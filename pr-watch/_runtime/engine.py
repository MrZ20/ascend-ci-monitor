"""Independent PR Watch cache, matching rules and Markdown renderer.

No network access or repository writes. The collector supplies verified data.
All timestamps are ISO-8601 with an offset; naive timestamps are rejected.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from functools import lru_cache
import fnmatch
import hashlib
import json
from pathlib import Path
import sqlite3
from typing import Any
from zoneinfo import ZoneInfo

import yaml

UTC = timezone.utc
SHANGHAI = ZoneInfo("Asia/Shanghai")
SCHEMA_VERSION = 1
CI_LABELS = {"passed": "通过", "failed": "失败", "pending": "运行中", "unknown": "未知"}


def instant(value: str | datetime | None = None) -> datetime:
    if value is None:
        return datetime.now(UTC)
    result = value if isinstance(value, datetime) else datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone-aware timestamp required")
    return result.astimezone(UTC)


def iso(value: str | datetime | None = None) -> str:
    return instant(value).isoformat(timespec="seconds").replace("+00:00", "Z")


def display_time(value: str | None, full: bool = False) -> str:
    if not value:
        return "未知"
    return instant(value).astimezone(SHANGHAI).strftime("%Y-%m-%d %H:%M:%S" if full else "%m-%d %H:%M")


def _text(value: Any) -> str:
    text = " ".join(str(value or "").split())
    for a, b in (("\\", "\\\\"), ("&", "&amp;"), ("<", "&lt;"), (">", "&gt;"), ("[", "\\["), ("]", "\\]"), ("*", "\\*"), ("_", "\\_"), ("`", "\\`")):
        text = text.replace(a, b)
    return text


def glob_match(path: str, pattern: str) -> bool:
    """POSIX segment glob: ** matches zero or more complete path segments."""
    parts, pats = tuple(path.split("/")), tuple(pattern.lstrip("/").split("/"))

    @lru_cache(None)
    def match(i: int, j: int) -> bool:
        if j == len(pats):
            return i == len(parts)
        if pats[j] == "**":
            return match(i, j + 1) or (i < len(parts) and match(i + 1, j))
        return i < len(parts) and fnmatch.fnmatchcase(parts[i], pats[j]) and match(i + 1, j + 1)
    return match(0, 0)


class Rules:
    def __init__(self, path: str | Path):
        raw = Path(path).read_bytes()
        data = yaml.safe_load(raw)
        if not isinstance(data, dict) or not isinstance(data.get("keep"), list) or not isinstance(data.get("exclude"), list):
            raise ValueError("rules require keep and exclude lists")
        if not all(isinstance(p, str) and p and ".." not in p.split("/") for p in data["keep"] + data["exclude"]):
            raise ValueError("invalid path pattern")
        self.keep, self.exclude = data["keep"], data["exclude"]
        self.policy_version = int(data.get("version", 1))
        self.version = hashlib.sha256(raw).hexdigest()

    def included(self, path: str) -> bool:
        return any(glob_match(path, p) for p in self.keep) or not any(glob_match(path, p) for p in self.exclude)

    def matched_paths(self, files: list[dict | str]) -> list[str]:
        paths = set()
        for f in files:
            candidates = [f] if isinstance(f, str) else [f.get("filename") or f.get("path"), f.get("previous_filename") or f.get("previous_path")]
            for p in candidates:
                if p and self.included(p):
                    paths.add(p)
        return sorted(paths)

    def matches(self, files: list[dict | str]) -> bool:
        return bool(self.matched_paths(files))

    def engineering_path(self, path: str) -> bool:
        """Unambiguous engineering paths; generic tools/common still need review."""
        if not self.included(path):
            return False
        name = path.rsplit('/', 1)[-1]
        if path.startswith('.github/'):
            return True
        if name.startswith(('Dockerfile', 'requirements')):
            return True
        if path.startswith(('docs/hooks/', 'docs/overrides/', 'docs/source/getting_started/',
                            'docs/source/developer_guide/contribution/', 'docs/source/javascripts/',
                            'docs/source/stylesheets/', 'tests/e2e/doctests/')):
            return True
        return path in {'mkdocs.yml', 'CMakeLists.txt', 'pyproject.toml', 'setup.py', 'setup.cfg',
                        'docs/Makefile', 'docs/README.md', 'docs/source/developer_guide/index.md',
                        'docs/source/community/slash-commands.md', 'csrc/build_aclnn.sh',
                        'csrc/build.sh', 'csrc/scripts/build_cache.py'}


def aggregate_ci(checks: list[dict], statuses: list[dict] | None = None, complete: bool = True) -> dict:
    """Aggregate already-selected authoritative checks; no ref selection here."""
    statuses = statuses or []
    failures, pending, gate = False, False, False
    failed = {"failure", "error", "timed_out", "cancelled", "action_required", "startup_failure", "stale"}
    for check in checks:
        conclusion = str(check.get("conclusion") or "").lower()
        state = str(check.get("status") or "").lower()
        bad = conclusion in failed
        failures |= bad
        gate |= bad and str(check.get("name", "")).lower() == "ci-gate"
        pending |= not conclusion or state not in ("", "completed")
        if conclusion and conclusion not in failed | {"success", "neutral", "skipped"}:
            complete = False
    for status in statuses:
        state = str(status.get("state") or "").lower()
        failures |= state in failed
        gate |= state in failed and str(status.get("context", "")).lower() == "ci-gate"
        pending |= state in {"pending", "expected"}
        if state not in failed | {"success", "pending", "expected"}:
            complete = False
    result = "unknown" if not complete or not (checks or statuses) else "failed" if failures else "pending" if pending else "passed"
    return {"state": result, "ci_gate": gate if result == "failed" else False}


def normalize_meta(pr: dict) -> dict:
    get = lambda snake, camel: pr.get(snake, pr.get(camel))
    number = int(pr["number"])
    if number <= 0:
        raise ValueError("invalid PR number")
    head = get("head_sha", "headRefOid") or (pr.get("head") or {}).get("sha")
    base = get("base_ref", "baseRefName") or (pr.get("base") or {}).get("ref")
    created = get("created_at", "createdAt")
    updated = get("updated_at", "updatedAt") or created
    if not head or not base or not created:
        raise ValueError("incomplete PR metadata")
    return dict(number=number, title=str(pr["title"]), url=f"https://github.com/vllm-project/vllm-ascend/pull/{number}", created_at=iso(created), updated_at=iso(updated), head_sha=head, base_ref=base, draft=int(bool(pr.get("draft", pr.get("isDraft", False)))))


class WatchDB:
    def __init__(self, db_path: str | Path, rules_path: str | Path):
        self.rules = Rules(rules_path)
        self.conn = sqlite3.connect(str(db_path))
        self.conn.row_factory = sqlite3.Row
        version = self.conn.execute("PRAGMA user_version").fetchone()[0]
        if version not in (0, SCHEMA_VERSION):
            raise ValueError("unsupported database schema")
        tables = {r[0] for r in self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if tables and not tables <= {"prs", "summaries", "metadata"}:
            raise ValueError("not a PR Watch database")
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS prs (
          number INTEGER PRIMARY KEY, title TEXT NOT NULL, url TEXT NOT NULL,
          created_at TEXT NOT NULL, updated_at TEXT NOT NULL, head_sha TEXT NOT NULL,
          base_ref TEXT NOT NULL, draft INTEGER NOT NULL,
          state TEXT NOT NULL DEFAULT 'open', first_discovered_at TEXT NOT NULL,
          meaningful_updated_at TEXT NOT NULL, last_seen_at TEXT NOT NULL,
          activity_at TEXT, activity_kind TEXT, activity_evidence TEXT,
          activity_probe_at TEXT, activity_probe_result TEXT,
          changed_files TEXT, files_sha TEXT, files_base TEXT, rules_version TEXT,
          matched INTEGER, matched_paths TEXT, additions INTEGER, deletions INTEGER,
          latest_commit_at TEXT, detail_sha TEXT, detail_base TEXT,
          summary TEXT, summary_sha TEXT, summary_base TEXT,
          ci_state TEXT NOT NULL DEFAULT 'unknown', ci_gate INTEGER NOT NULL DEFAULT 0,
          ci_verified_state TEXT, ci_verified_gate INTEGER,
          ci_checked_at TEXT, ci_success_at TEXT, ci_attempted_at TEXT,
          ci_deferred_at TEXT, ci_deferred_reason TEXT, ci_sha TEXT, ci_base TEXT,
          final_at TEXT, detail_error TEXT, ci_error TEXT
        );
        CREATE TABLE IF NOT EXISTS summaries (
          number INTEGER NOT NULL, head_sha TEXT NOT NULL, base_ref TEXT NOT NULL,
          summary TEXT NOT NULL, PRIMARY KEY(number, head_sha, base_ref)
        );
        CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        PRAGMA user_version=1;
        """)
        columns = {r[1] for r in self.conn.execute("PRAGMA table_info(prs)")}
        migrate_ci_success = "ci_success_at" not in columns
        migrate_ci_attempt = "ci_attempted_at" not in columns
        for name, kind in (("ci_verified_state", "TEXT"), ("ci_verified_gate", "INTEGER"),
                           ("ci_success_at", "TEXT"), ("ci_attempted_at", "TEXT"),
                           ("ci_deferred_at", "TEXT"), ("ci_deferred_reason", "TEXT"),
                           ("activity_at", "TEXT"), ("activity_kind", "TEXT"), ("activity_evidence", "TEXT"),
                           ("activity_probe_at", "TEXT"), ("activity_probe_result", "TEXT")):
            if name not in columns:
                self.conn.execute(f"ALTER TABLE prs ADD COLUMN {name} {kind}")
        if migrate_ci_attempt:
            # Old budget-deferred rows could also carry ci_checked_at despite
            # no request being made. Error rows cannot prove a real attempt.
            self.conn.execute("UPDATE prs SET ci_attempted_at=ci_checked_at WHERE ci_error IS NULL")
        if migrate_ci_success:
            # The legacy field was also updated on failed fetches. Only a row
            # without an error proves that timestamp was a complete refresh.
            self.conn.execute("UPDATE prs SET ci_success_at=ci_checked_at WHERE ci_error IS NULL")
            self.conn.execute("UPDATE prs SET ci_checked_at=NULL WHERE ci_error IS NOT NULL")
        # Recover only source-dated activity. First discovery, PR updated_at and
        # meaningful_updated_at are observations, never proof of past activity.
        for row in self.conn.execute("SELECT number,created_at,latest_commit_at FROM prs WHERE activity_at IS NULL").fetchall():
            candidates = [(iso(row["created_at"]), "created", "GitHub PR created_at")]
            if row["latest_commit_at"]:
                candidates.append((iso(row["latest_commit_at"]), "commit", "Cached latest Commit timestamp"))
            at, kind, evidence = max(candidates, key=lambda v: instant(v[0]))
            self.conn.execute("UPDATE prs SET activity_at=?,activity_kind=?,activity_evidence=? WHERE number=?", (at, kind, evidence, row["number"]))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def row(self, number: int) -> dict | None:
        row = self.conn.execute("SELECT * FROM prs WHERE number=?", (number,)).fetchone()
        if not row:
            return None
        data = dict(row)
        for key in ("changed_files", "matched_paths"):
            if data[key] is not None:
                data[key] = json.loads(data[key])
        return data

    def _meta(self, key: str, value: Any):
        self.conn.execute("INSERT OR REPLACE INTO metadata VALUES (?,?)", (key, json.dumps(value)))

    def _record_activity(self, number: int, activity_at: str, kind: str, evidence: str) -> bool:
        if kind not in {"created", "commit", "head", "base", "draft", "ci"}:
            raise ValueError("unsupported activity kind")
        if not isinstance(evidence, str) or not evidence.strip():
            raise ValueError("activity evidence required")
        at = iso(activity_at)
        row = self.row(number)
        if row is None:
            raise KeyError(number)
        if row["activity_at"] and instant(row["activity_at"]) >= instant(at):
            return False
        self.conn.execute("UPDATE prs SET activity_at=?,activity_kind=?,activity_evidence=? WHERE number=?", (at, kind, evidence.strip(), number))
        return True

    def record_activity(self, number: int, activity_at: str, kind: str, evidence: str) -> bool:
        """Record verified source activity, never comments or generic updated_at."""
        changed = self._record_activity(number, activity_at, kind, evidence)
        self.conn.commit()
        return changed

    def record_activity_probe(self, number: int, result: str, now=None):
        if result not in {"active", "inactive", "unknown"}:
            raise ValueError("unsupported activity probe result")
        row = self.row(number)
        if row is None:
            raise KeyError(number)
        if result == "active" and (not row["activity_at"] or instant(row["activity_at"]) < instant(now) - timedelta(days=30)):
            raise ValueError("active probe requires recent activity evidence")
        self.conn.execute("UPDATE prs SET activity_probe_at=?,activity_probe_result=? WHERE number=?", (iso(now), result, number))
        self.conn.commit()

    def scope_active(self, now=None) -> list[int]:
        """Open PRs with verified activity in the rolling previous 30 days."""
        cutoff = instant(now) - timedelta(days=30)
        known_open = self._last_complete_open_ids()
        return sorted(r["number"] for r in self.conn.execute("SELECT number,activity_at,matched FROM prs WHERE state='open'")
                      if r["activity_at"] and instant(r["activity_at"]) >= cutoff
                      and (known_open is None or r["number"] in known_open or r["matched"] == 1))

    def _last_complete_open_ids(self) -> set[int] | None:
        data = self.conn.execute("SELECT value FROM metadata WHERE key='complete_discovery'").fetchone()
        if data:
            snapshot = json.loads(data[0])
            # A newer partial page can prove presence (but never absence).
            return set(snapshot["open_ids"]) | {r[0] for r in self.conn.execute("SELECT number FROM prs WHERE last_seen_at>?", (snapshot["at"],))}
        # Legacy cache migration: a completed discovery stamped every seen PR.
        legacy = self.conn.execute("SELECT value FROM metadata WHERE key='discovery'").fetchone()
        if legacy:
            last = json.loads(legacy[0])
            if last.get("complete") and last.get("at"):
                return {r[0] for r in self.conn.execute("SELECT number FROM prs WHERE last_seen_at>=?", (last["at"],))}
        return None

    def ingest_discovery(self, prs: list[dict], complete: bool, now=None) -> dict:
        now = iso(now)
        normalized = [normalize_meta(pr) for pr in prs]
        numbers = [p["number"] for p in normalized]
        if len(numbers) != len(set(numbers)):
            raise ValueError("duplicate PR in discovery")
        needs_files = []
        for p in normalized:
            old = self.row(p["number"])
            if old is None:
                self.conn.execute("""INSERT INTO prs(number,title,url,created_at,updated_at,head_sha,base_ref,draft,first_discovered_at,meaningful_updated_at,last_seen_at)
                  VALUES(:number,:title,:url,:created_at,:updated_at,:head_sha,:base_ref,:draft,:now,:created_at,:now)""", dict(p, now=now))
                self._record_activity(p["number"], p["created_at"], "created", "GitHub PR created_at")
            else:
                change = old["head_sha"] != p["head_sha"] or old["base_ref"] != p["base_ref"] or old["draft"] != p["draft"] or old["state"] != "open"
                self.conn.execute("""UPDATE prs SET title=:title,url=:url,created_at=:created_at,updated_at=:updated_at,
                    head_sha=:head_sha,base_ref=:base_ref,draft=:draft,state='open',last_seen_at=:now,
                    meaningful_updated_at=:meaningful,final_at=NULL WHERE number=:number""", dict(p, now=now, meaningful=now if change else old["meaningful_updated_at"]))
                for key, kind in (("head_sha", "head"), ("base_ref", "base"), ("draft", "draft")):
                    if old[key] != p[key]:
                        self._record_activity(p["number"], now, kind, f"Observed {key} change from {old[key]} to {p[key]}")
                if old["updated_at"] != p["updated_at"]:
                    self.conn.execute("UPDATE prs SET activity_probe_at=NULL,activity_probe_result=NULL WHERE number=?", (p["number"],))
            row = self.row(p["number"])
            if row["changed_files"] is None or row["files_sha"] != p["head_sha"] or row["files_base"] != p["base_ref"]:
                if row["activity_at"] and instant(row["activity_at"]) >= instant(now) - timedelta(days=30):
                    needs_files.append(p["number"])
            elif row["rules_version"] != self.rules.version:
                paths = self.rules.matched_paths(row["changed_files"])
                self.conn.execute("UPDATE prs SET matched=?,matched_paths=?,rules_version=?,meaningful_updated_at=? WHERE number=?", (bool(paths), json.dumps(paths), self.rules.version, row["meaningful_updated_at"], p["number"]))
        existing = [r[0] for r in self.conn.execute("SELECT number FROM prs WHERE state='open'")]
        missing = sorted(set(existing) - set(numbers)) if complete else []
        self._meta("discovery", {"at": now, "complete": bool(complete), "count": len(numbers)})
        if complete:
            self._meta("complete_discovery", {"at": now, "open_ids": numbers})
        self.conn.commit()
        if self.rules.policy_version >= 2:
            self.rematch_cached()
        return {"needs_files": needs_files, "missing": missing}

    def scope_decision(self, row: dict) -> dict | None:
        if self.rules.policy_version < 2:
            return {'decision': 'include', 'reason': 'v1 path policy'}
        paths = self.rules.matched_paths(row.get('changed_files') or [])
        if not paths:
            return {'decision': 'exclude', 'reason': 'explicit path exclusion'}
        if any(self.rules.engineering_path(p) for p in paths):
            return {'decision': 'include', 'reason': 'explicit engineering file'}
        saved = self.conn.execute("SELECT value FROM metadata WHERE key=?", (f"scope:{row['number']}",)).fetchone()
        if not saved:
            return None
        value = json.loads(saved[0])
        if (value.get('head_sha'), value.get('base_ref'), value.get('rules_version')) != (row['head_sha'], row['base_ref'], self.rules.version):
            return None
        return value

    def apply_scope_decision(self, number: int, decision: str, reason: str, head_sha: str, base_ref: str):
        row = self.row(number)
        if row is None or (head_sha, base_ref) != (row['head_sha'], row['base_ref']):
            raise ValueError('stale semantic decision')
        if decision not in {'include', 'exclude', 'uncertain'} or not reason.strip():
            raise ValueError('semantic decision and evidence reason required')
        paths = self.rules.matched_paths(row['changed_files'] or [])
        if decision != 'include' and any(self.rules.engineering_path(p) for p in paths):
            raise ValueError('cannot semantically exclude explicit engineering files')
        if decision == 'include' and not paths:
            raise ValueError('cannot override explicit path exclusions')
        self._meta(f'scope:{number}', dict(decision=decision, reason=reason, head_sha=head_sha,
                    base_ref=base_ref, rules_version=self.rules.version))
        self.conn.execute('UPDATE prs SET matched=? WHERE number=?', (decision == 'include', number))
        self.conn.commit()

    def rematch_cached(self):
        """Reclassify cached complete file sets, including archived entries, without network."""
        for record in self.conn.execute('SELECT number FROM prs WHERE changed_files IS NOT NULL').fetchall():
            row = self.row(record[0])
            if row['files_sha'] != row['head_sha'] or row['files_base'] != row['base_ref']:
                continue
            paths = self.rules.matched_paths(row['changed_files'])
            decision = self.scope_decision(row)
            matched = bool(paths) and bool(decision and decision['decision'] == 'include')
            self.conn.execute('UPDATE prs SET matched=?,matched_paths=?,rules_version=? WHERE number=?',
                              (matched, json.dumps(paths), self.rules.version, row['number']))
        self.conn.commit()

    def semantic_pending(self, now=None):
        active = set(self.scope_active(now))
        return [self.row(r[0]) for r in self.conn.execute("SELECT number FROM prs WHERE state='open' AND changed_files IS NOT NULL AND files_sha=head_sha AND files_base=base_ref")
                if r[0] in active and self.scope_decision(self.row(r[0])) is None]

    def cached_summary(self, number: int, head_sha: str | None = None, base_ref: str | None = None) -> str | None:
        row = self.row(number)
        if row is None:
            return None
        found = self.conn.execute("SELECT summary FROM summaries WHERE number=? AND head_sha=? AND base_ref=?", (number, head_sha or row["head_sha"], base_ref or row["base_ref"])).fetchone()
        return found[0] if found else None

    def update_detail(self, number: int, files: list[dict | str], additions: int | None = None, deletions: int | None = None,
                      latest_commit_at: str | None = None, summary: str | None = None, summary_sha: str | None = None,
                      now=None, files_complete: bool = True, head_sha: str | None = None, base_ref: str | None = None):
        row = self.row(number)
        if row is None:
            raise KeyError(number)
        if head_sha and head_sha != row["head_sha"] or base_ref and base_ref != row["base_ref"]:
            raise ValueError("stale detail SHA/base")
        if not files_complete:
            self.conn.execute("UPDATE prs SET detail_error='changed-files pagination incomplete' WHERE number=?", (number,))
            self.conn.commit()
            return False
        paths = self.rules.matched_paths(files)
        # Validate everything before changing rows, so stale/invalid detail cannot
        # be accidentally committed by a later successful operation.
        latest = None
        if paths and additions is not None and deletions is not None and latest_commit_at is not None:
            if not isinstance(additions, int) or not isinstance(deletions, int) or additions < 0 or deletions < 0:
                raise ValueError("invalid line count")
            latest = iso(latest_commit_at)
        if paths and summary is not None:
            if summary_sha != row["head_sha"]:
                raise ValueError("summary must have exact current SHA")
            summary = " ".join(summary.split())
            if not summary:
                raise ValueError("empty summary")
        self.conn.execute("UPDATE prs SET changed_files=?,files_sha=?,files_base=?,rules_version=?,matched=?,matched_paths=?,detail_error=NULL WHERE number=?", (json.dumps(files, ensure_ascii=False), row["head_sha"], row["base_ref"], self.rules.version, bool(paths), json.dumps(paths, ensure_ascii=False), number))
        if paths:
            if additions is None or deletions is None or latest_commit_at is None:
                self.conn.execute("UPDATE prs SET detail_error='matched PR detail incomplete' WHERE number=?", (number,))
            else:
                self.conn.execute("UPDATE prs SET additions=?,deletions=?,latest_commit_at=?,detail_sha=?,detail_base=? WHERE number=?", (additions, deletions, latest, row["head_sha"], row["base_ref"], number))
                self._record_activity(number, latest, "commit", f"GitHub latest Commit timestamp for {row['head_sha']}")
            if summary is not None:
                self.conn.execute("INSERT OR REPLACE INTO summaries VALUES (?,?,?,?)", (number, row["head_sha"], row["base_ref"], summary))
            cached = self.cached_summary(number)
            if cached:
                self.conn.execute("UPDATE prs SET summary=?,summary_sha=?,summary_base=? WHERE number=?", (cached, row["head_sha"], row["base_ref"], number))
        self.conn.commit()
        if self.rules.policy_version >= 2:
            self.rematch_cached()
        return bool(paths)

    def update_ci(self, number: int, state: str, ci_gate=False, now=None, complete=True, head_sha=None, base_ref=None, activity_at=None):
        row = self.row(number)
        if row is None:
            raise KeyError(number)
        if head_sha and head_sha != row["head_sha"] or base_ref and base_ref != row["base_ref"]:
            raise ValueError("stale CI SHA/base")
        if row["state"] != "open":
            raise ValueError("closed PR CI is frozen")
        now = iso(now)
        if not complete:
            self.conn.execute("UPDATE prs SET ci_attempted_at=?,ci_error=? WHERE number=?", (now,"CI coverage incomplete; last known result retained",number))
            self.conn.commit()
            return
        state = state
        if state not in CI_LABELS:
            raise ValueError("unsupported CI state")
        ci_gate = bool(ci_gate) and state == "failed"
        actual_activity = iso(activity_at) if activity_at is not None else None
        # A read failure is a coverage event, not evidence of a meaningful CI change.
        changed = complete and (state != (row["ci_verified_state"] or "unknown") or ci_gate != bool(row["ci_verified_gate"]))
        self.conn.execute("""UPDATE prs SET ci_state=?,ci_gate=?,ci_checked_at=?,ci_success_at=?,ci_attempted_at=?,
            ci_deferred_at=NULL,ci_deferred_reason=NULL,ci_sha=?,ci_base=?,
            meaningful_updated_at=?,ci_error=?,ci_verified_state=?,ci_verified_gate=? WHERE number=?""", (
                state, ci_gate, now if complete else row["ci_success_at"], now if complete else row["ci_success_at"], now,
                row["head_sha"], row["base_ref"], now if changed else row["meaningful_updated_at"],
                None if complete else "CI coverage incomplete", state if complete else row["ci_verified_state"],
                ci_gate if complete else row["ci_verified_gate"], number))
        if complete and actual_activity is not None:
            self._record_activity(number, actual_activity, "ci", f"GitHub Check/Status timestamp for {row['head_sha']}")
        self.conn.commit()

    def mark_ci_deferred(self, numbers: list[int], now=None, reason="budget"):
        """Record unattempted work without changing CI state or refresh clocks."""
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("deferred reason required")
        at = iso(now)
        numbers = list(dict.fromkeys(numbers))
        if any(self.row(number) is None for number in numbers):
            raise KeyError("unknown deferred PR")
        for number in numbers:
            self.conn.execute("UPDATE prs SET ci_deferred_at=?,ci_deferred_reason=? WHERE number=? AND state='open'", (at, reason.strip(), number))
        self.conn.commit()

    def ci_due(self, now=None) -> list[int]:
        now = instant(now)
        local = now.astimezone(SHANGHAI)
        due = []
        in_scope = set(self.scope_active(now))
        for record in self.conn.execute("SELECT * FROM prs WHERE state='open' AND matched=1"):
            row = dict(record)
            if row["number"] not in in_scope:
                continue
            stale = row["ci_sha"] != row["head_sha"] or row["ci_base"] != row["base_ref"]
            active = instant(row["meaningful_updated_at"]) >= now - timedelta(hours=72) or row["ci_state"] in ("pending", "unknown") or stale
            checked = instant(row["ci_success_at"]) if row["ci_success_at"] else None
            needs_refresh = False
            if active:
                needs_refresh = stale or not checked or bool(row["ci_error"]) or now.replace(minute=0,second=0,microsecond=0) > checked.replace(minute=0,second=0,microsecond=0)
            else:
                checkpoint = local.replace(hour=9, minute=0, second=0, microsecond=0)
                needs_refresh = bool(row["ci_error"]) or local >= checkpoint and (not checked or checked < checkpoint.astimezone(UTC))
            if needs_refresh:
                due.append(row)
        oldest = datetime.min.replace(tzinfo=UTC)
        # Eligibility uses successful refreshes. Scheduling rotates by actual
        # attempts, so a permanently failing endpoint cannot monopolize the queue.
        due.sort(key=lambda r: (instant(r["ci_attempted_at"]) if r["ci_attempted_at"] else oldest,
                                instant(r["ci_success_at"]) if r["ci_success_at"] else oldest,
                                r["number"]))
        return [r["number"] for r in due]

    def confirm_closed(self, number: int, state: str, closed_at: str, merged_at: str | None = None):
        if state not in ("merged", "closed"):
            raise ValueError("explicit final state required")
        row = self.row(number)
        if row is None:
            raise KeyError(number)
        final = iso(merged_at if state == "merged" and merged_at else closed_at)
        self.conn.execute("UPDATE prs SET state=?,final_at=? WHERE number=?", (state, final, number))
        self.conn.commit()

    def render(self, now=None) -> tuple[str, str]:
        now = instant(now)
        if self.rules.policy_version >= 2:
            self.rematch_cached()
        in_scope = set(self.scope_active(now))
        active = [dict(r) for r in self.conn.execute("SELECT * FROM prs WHERE state='open' AND matched=1 ORDER BY created_at DESC, number DESC") if r["number"] in in_scope]
        archived = [dict(r) for r in self.conn.execute("SELECT * FROM prs WHERE state IN ('merged','closed') AND matched=1 ORDER BY final_at DESC, number DESC")]
        pending = sum(1 for r in self.conn.execute("""SELECT number FROM prs WHERE state='open' AND
            (matched IS NULL OR files_sha != head_sha OR files_base != base_ref OR detail_error IS NOT NULL
            OR (matched=1 AND (detail_sha IS NULL OR detail_sha != head_sha OR detail_base != base_ref
                OR summary_sha IS NULL OR summary_sha != head_sha OR summary_base != base_ref)))""") if r["number"] in in_scope)
        cutoff = now - timedelta(days=30)
        known_open = self._last_complete_open_ids()
        activity_unknown = sum(1 for r in self.conn.execute("SELECT number,created_at,updated_at,activity_probe_result FROM prs WHERE state='open'")
                               if r["number"] not in in_scope and (known_open is None or r["number"] in known_open)
                               and instant(r["created_at"]) < cutoff and instant(r["updated_at"]) >= cutoff and r["activity_probe_result"] != "inactive")
        discovery = self.conn.execute("SELECT value FROM metadata WHERE key='discovery'").fetchone()
        complete = json.loads(discovery[0]).get("complete", False) if discovery else False
        lines = ["# PR 关注列表", "", f"最近刷新：{display_time(iso(now), True)}（上海时间）", f"当前关注的开放 PR：{len(active)}", "范围：最近 30 天有创建、提交、CI、Draft 或目标分支变化证据的开放 PR；普通评论不算活动。", "长期无元数据更新的旧 PR 未逐个追查仅 CI 重跑的活动，本页不代表这类活动已全覆盖。", ""]
        bounded = self.conn.execute("SELECT value FROM metadata WHERE key='bounded_discovery'").fetchone()
        if bounded:
            pending = sum(1 for r in active if r['files_sha'] != r['head_sha'] or r['detail_sha'] != r['head_sha'])
            activity_unknown = 0
            complete = True
            lines += ["发现范围：仅限最近更新候选，每轮最多 300 个；已有关注 PR 按编号独立刷新。已取消旧历史初始化补齐，不承诺全量开放列表覆盖。", ""]
        if activity_unknown:
            lines += [f"活动待确认：{activity_unknown} 个较早创建、近期 updated_at 变化的开放 PR 尚无最近 30 天有效活动证据，暂不纳入。", ""]
        final_pending = sum(1 for r in active if known_open is not None and r["number"] not in known_open)
        if final_pending:
            lines += [f"最终状态待确认：{final_pending} 个已跟踪 PR 不在最近完整开放列表中，保留显示，尚未归档。", ""]
        ci_pending = set(self.ci_due(now)) | {r["number"] for r in active if r["ci_deferred_at"]}
        if ci_pending:
            lines += [f"CI 待刷新：{len(ci_pending)} 个 PR 尚未取得本轮所需的完整检查结果；上次状态不代表当前结果。", ""]
        if not complete or pending:
            lines += [f"覆盖说明：{'开放 PR 列表尚未完整获取；' if not complete else ''}{f'{pending} 个近 30 天范围内的 PR 文件范围或详情待补齐。' if pending else '未据此归档缺失 PR。'}", ""]
        semantic_pending = self.semantic_pending(now) if self.rules.policy_version >= 2 else []
        if semantic_pending:
            lines += [f"范围待判断：{len(semantic_pending)} 个 PR 的工具、通用目录或新路径尚待轻量语义核对，暂不纳入关注列表。", ""]
        lines += ["## 最近更新（72h）", ""]
        recent = sorted([r for r in active if instant(r["activity_at"] or r["created_at"]) >= now - timedelta(hours=72)], key=lambda r: (r["activity_at"] or r["created_at"], r["number"]), reverse=True)
        lines += [f"- [{display_time(r['activity_at'] or r['created_at'])} · #{r['number']} {_text(r['title'])}](#pr-{r['number']})" for r in recent] or ["暂无近期更新。"]
        lines += ["", "## 当前关注", ""]
        for row in active:
            lines += self._section(row, ci_pending=row["number"] in ci_pending)
        if not active:
            lines += ["当前没有已确认符合范围的开放 PR。", ""]
        archive = ["# PR 归档", "", f"最近刷新：{display_time(iso(now), True)}（上海时间）", "", "仅记录开始跟踪后确认合入或关闭的 PR，不追溯全部历史。", ""]
        removed = self.conn.execute("SELECT value FROM metadata WHERE key='archive_pruned'").fetchone()
        if removed:
            archive += ['<!-- pr-watch-pruned: '+json.dumps(json.loads(removed[0]))+' -->', '']
        for row in archived:
            archive += self._section(row, archived=True)
        if not archived:
            archive += ["暂无归档。", ""]
        return "\n".join(lines), "\n".join(archive)

    @staticmethod
    def _section(row: dict, archived=False, ci_pending=False) -> list[str]:
        fresh_summary = row["summary_sha"] == row["head_sha"] and row["summary_base"] == row["base_ref"]
        fresh_detail = row["detail_sha"] == row["head_sha"] and row["detail_base"] == row["base_ref"]
        fresh_ci = row["ci_sha"] == row["head_sha"] and row["ci_base"] == row["base_ref"]
        ci = CI_LABELS[row["ci_state"]] if fresh_ci else "未知"
        if fresh_ci and row["ci_state"] == "failed" and row["ci_gate"]:
            ci += "（ci-gate）"
        if ci_pending and not archived:
            previous = CI_LABELS.get(row["ci_verified_state"], "未知")
            if row["ci_verified_state"] == "failed" and row["ci_verified_gate"]:
                previous += "（ci-gate）"
            ci = f"{previous}（最近已知；待刷新；上次完整检查：{display_time(row['ci_success_at'])}；{'当前提交' if fresh_ci else '旧提交'}）" if row["ci_success_at"] else "未知（待刷新；尚无完整检查记录）"
        changes = f"+{row['additions']} / -{row['deletions']}" if fresh_detail else "待更新"
        summary = row["summary"] if fresh_summary and row["summary"] else "相关文件已纳入关注，当前提交的变更摘要待补齐。"
        status = f"**CI：** {ci} · **改动：** {changes} · **最后提交：** {display_time(row['latest_commit_at']) if fresh_detail else '待更新'}"
        if row["draft"] and not archived:
            status += " · **Draft**"
        if archived:
            status += f" · **{'已合入' if row['state'] == 'merged' else '已关闭'}：** {display_time(row['final_at'], True)}"
        return [f'<a id="pr-{row["number"]}"></a>', "", f'### [#{row["number"]} · {_text(row["title"])}]({row["url"]})', "", _text(summary), "", status, ""]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", required=True)
    parser.add_argument("--input", help="verified collector batch JSON")
    parser.add_argument("--now")
    args = parser.parse_args()
    directory = Path(args.directory)
    db = WatchDB(directory / "pr_watch.db", directory / "exclude.yaml")
    results = {}
    if args.input:
        batch = json.loads(Path(args.input).read_text())
        now = batch.get("now", args.now)
        if "prs" in batch:
            results["discovery"] = db.ingest_discovery(batch["prs"], batch.get("discovery_complete", False), now)
        for detail in batch.get("details", []):
            db.update_detail(**dict(detail, now=now))
        for ci in batch.get("ci", []):
            db.update_ci(**dict(ci, now=now))
        for closed in batch.get("closed", []):
            db.confirm_closed(**closed)
    active, archive = db.render(args.now)
    (directory / "active.md").write_text(active)
    (directory / "archive.md").write_text(archive)
    results["ci_due"] = db.ci_due(args.now)
    print(json.dumps(results, ensure_ascii=False))
    db.close()


if __name__ == "__main__":
    main()
