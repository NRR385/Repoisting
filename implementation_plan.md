# Reposting — Implementation Plan

> **Planning document only. No code changes have been made.**
> Repository: `https://github.com/NRR385/Reposting`
> Last updated: 2026-09-17

---

## Table of Contents

1. [Current State](#phase-0--current-state)
2. [Phase 1 — Project Foundation](#phase-1--project-foundation)
3. [Phase 2 — Core Data Models](#phase-2--core-data-models)
4. [Phase 3 — Validation](#phase-3--validation)
5. [Phase 4 — Local Storage](#phase-4--local-storage)
6. [Phase 5 — Repost Queue](#phase-5--repost-queue)
7. [Phase 6 — Mock Repost Adapter](#phase-6--mock-repost-adapter)
8. [Phase 7 — CLI Experience](#phase-7--cli-experience)
9. [Phase 8 — Scheduling](#phase-8--scheduling)
10. [Phase 9 — Statistics & History](#phase-9--statistics--history)
11. [Phase 10 — Testing & Reliability](#phase-10--testing--reliability)
12. [Phase 11 — GitHub / Open Source](#phase-11--github--open-source)
13. [Phase 12 — Release Preparation](#phase-12--release-preparation)
14. [Phase 13 — Future Platform Integrations](#phase-13--future-platform-integrations)
15. [MVP Definition](#mvp-definition)
16. [Architecture](#architecture)
17. [Data Design](#data-design)
18. [CLI Design](#cli-design)
19. [Storage Design](#storage-design)
20. [Testing Architecture](#testing-architecture)
21. [GitHub / Open-Source Strategy](#githubopen-source-strategy)
22. [Release Roadmap](#release-roadmap)
23. [Security & Reliability](#security--reliability)
24. [Final Implementation Order](#final-implementation-order)

---

## File Status Legend

Throughout this document, files are tagged as follows:

| Tag | Meaning |
|---|---|
| `[EXISTS]` | File already in the repository right now |
| `[PHASE N]` | File first introduced in Phase N |
| `[FUTURE]` | File planned for a phase not yet numbered / post-MVP |
| `[DELETED]` | File to be removed during this phase |

---

## Phase 0 — Current State

### Goal
Establish the exact baseline of what the repository currently contains before
any development begins.

### Current repository (the real starting point)

```
Reposting/
├── README.md                   [EXISTS]  — "Coming Soon" placeholder
├── main.py                     [EXISTS]  — minimal entry point stub
└── implementation_plan.md      [EXISTS]  — this document
```

**That is the entire repository. Nothing else exists.**

### What `main.py` contains today

```python
"""
Reposting - A modular content reposting automation toolkit.

This project is currently under development.
"""


def main() -> None:
    """Entry point for the application."""
    print("🚧 Reposting is coming soon!")


if __name__ == "__main__":
    main()
```

*It runs. It prints a message. It is a placeholder.*

### What `README.md` contains today

```markdown
### Reposting — A modular content reposting automation toolkit
  **Coming Soon**

- This project is currently under development.
- The goal is to build a modular toolkit for managing, scheduling,
  and tracking content reposting through a clean and extensible architecture.
More details, features, documentation, and usage instructions will be added
as development progresses.
```

*It is intentionally a placeholder and should remain so until Phase 11.*

### What does NOT exist yet

Everything else. In particular, the following do **not** exist and should **not**
be assumed to exist until their respective phase:

| File / directory | Introduced in |
|---|---|
| `.gitignore` | Phase 1 |
| `.python-version` | Phase 1 |
| `pyproject.toml` | Phase 1 |
| `CONTRIBUTING.md` | Phase 1 |
| `reposting/` package | Phase 1 |
| `tests/` directory | Phase 2 |
| `.github/` directory | Phase 11 |
| `docs/` directory | Phase 11 |
| `LICENSE` | Phase 1 |
| `CHANGELOG.md` | Phase 11 |
| `SECURITY.md` | Phase 11 |
| `data/` directory | Runtime only (never committed) |

### What currently works

| Action | Result |
|---|---|
| `python main.py` | ✅ Runs; prints the "Coming Soon" message |
| Any other `reposting` functionality | ❌ Does not exist |

### Git state

- **Branch**: `main`
- **Remote**: `https://github.com/NRR385/Reposting.git`
- **Working tree**: clean (only 3 files tracked)
- **No tests, no CI, no packaging, no dependencies**

### Design decisions made before Phase 1

These decisions are locked in regardless of phase:

1. **Python 3.11+** — minimum supported version.
2. **Zero runtime dependencies in MVP** — standard library only.
3. **Dev dependencies**: `pytest` and `ruff` only (no other tools).
4. **Modular package architecture** — `reposting/` sub-packages per concern.
5. **JSON storage for MVP**, SQLite considered post-MVP.
6. **Mock adapter first** — no real platform integrations until post-v1.0.0.
7. **Conventional Commits** — commit message format from day one.
8. **`README.md` stays as "Coming Soon"** until Phase 11 (real functionality ships first).

---

## Phase 1 — Project Foundation

### Goal
Transform the minimal 3-file repository into a professional, installable, and
contributor-ready Python project — before writing any functional code.

### Why it exists
Every phase from Phase 2 onwards depends on having: a proper package structure,
an installable package (`pyproject.toml`), a linter/formatter, a test runner,
and a way to ignore generated files. Building this foundation first means every
subsequent phase can follow the same conventions without retrofitting them.

### Features
- Add `.gitignore` — prevents `__pycache__`, `.venv`, `data/`, `.env` from polluting commits.
- Add `.python-version` — pins Python 3.11 for all contributors.
- Add `pyproject.toml` — makes the project installable via `pip install -e ".[dev]"`.
- Add `LICENSE` — MIT, referenced in `pyproject.toml`.
- Create `reposting/` package — the installable Python package.
  - `reposting/__init__.py` — version string `"0.1.0"`.
  - `reposting/__main__.py` — enables `python -m reposting`.
  - `reposting/cli/__init__.py` — placeholder.
  - `reposting/cli/commands.py` — minimal `main()` with `--version` flag only.
- Update `main.py` — thin shim that calls `reposting.cli.commands.main()`.
- Add `CONTRIBUTING.md` — setup guide, commit convention, PR process.
- Add `.github/workflows/ci.yml` — lint + test CI on push/PR to `main`.
- Add `.github/ISSUE_TEMPLATE/bug_report.md`.
- Add `.github/ISSUE_TEMPLATE/feature_request.md`.
- Add `.github/PULL_REQUEST_TEMPLATE.md`.

### Files

```
[EXISTS]  README.md                           — unchanged (still "Coming Soon")
[EXISTS]  main.py                             — MODIFIED: thin shim to reposting.cli
[EXISTS]  implementation_plan.md              — unchanged

[PHASE 1] .gitignore
[PHASE 1] .python-version
[PHASE 1] pyproject.toml
[PHASE 1] LICENSE
[PHASE 1] CONTRIBUTING.md
[PHASE 1] reposting/__init__.py
[PHASE 1] reposting/__main__.py
[PHASE 1] reposting/cli/__init__.py
[PHASE 1] reposting/cli/commands.py           — stub: --version only
[PHASE 1] .github/workflows/ci.yml
[PHASE 1] .github/ISSUE_TEMPLATE/bug_report.md
[PHASE 1] .github/ISSUE_TEMPLATE/feature_request.md
[PHASE 1] .github/PULL_REQUEST_TEMPLATE.md
```

### Technical design

```
python main.py --version
       ↓
main.py (shim)
       ↓
reposting/cli/commands.py → main()
       ↓
argparse → --version → prints "reposting 0.1.0"
```

**`pyproject.toml` key decisions:**
- `name = "reposting"`, `version = "0.1.0"`
- `requires-python = ">=3.11"`
- `dependencies = []` — zero runtime dependencies
- `[project.optional-dependencies] dev = ["pytest>=8.0", "pytest-cov>=5.0", "ruff>=0.4"]`
- `[project.optional-dependencies] scheduler = ["APScheduler>=3.10"]` — declared now, used in Phase 8
- `[project.scripts] reposting = "reposting.cli.commands:main"` — enables the `reposting` command

**CI (`ci.yml`) steps:**
1. `actions/checkout@v4`
2. `actions/setup-python@v5` with matrix `["3.11", "3.12"]`
3. `pip install -e ".[dev]"`
4. `ruff check .`
5. `ruff format --check .`
6. `pytest --tb=short -q`

> **Note:** CI will initially fail at the `pytest` step because no tests exist yet.
> Add an empty `tests/__init__.py` and a trivial passing test in this phase so CI is green.

### Dependencies

| Dependency | Type | Purpose |
|---|---|---|
| `pytest>=8.0` | dev | Test runner |
| `pytest-cov>=5.0` | dev | Coverage reporting |
| `ruff>=0.4` | dev | Linting and formatting |

No runtime dependencies.

### Testing
- Add `tests/__init__.py` (empty).
- Add `tests/test_placeholder.py` with one trivial passing test so CI is green.

```python
# tests/test_placeholder.py
def test_package_is_importable():
    import reposting
    assert reposting.__version__ == "0.1.0"
```

### GitHub issues

| Title | Description | Labels | Difficulty |
|---|---|---|---|
| Add `.gitignore` | Python standard + data/, .env | `good first issue`, `chore` | Beginner |
| Add `pyproject.toml` | PEP 517 metadata + dev extras | `enhancement`, `chore` | Beginner |
| Set up GitHub Actions CI | ruff + pytest on Python 3.11 and 3.12 | `ci` | Intermediate |
| Create `reposting/` package skeleton | `__init__.py`, `__main__.py`, CLI stub | `enhancement` | Beginner |
| Add `CONTRIBUTING.md` | Setup, commits, style, PR guide | `documentation` | Beginner |

### Definition of done
- [ ] `python main.py --version` prints `reposting 0.1.0`.
- [ ] `python -m reposting --version` prints `reposting 0.1.0`.
- [ ] `pip install -e ".[dev]"` succeeds without errors.
- [ ] `ruff check .` passes with zero issues.
- [ ] `pytest` passes (trivial import test).
- [ ] CI workflow runs and is green on GitHub.
- [ ] `__pycache__/`, `.venv/`, and `data/` are ignored by git.

### Commit strategy
```
chore: add .gitignore and .python-version
chore: add pyproject.toml with dev extras
chore: add MIT LICENSE
feat(package): create reposting package skeleton with version 0.1.0
feat(cli): add CLI stub with --version flag
chore(main): update main.py to delegate to reposting.cli
ci: add GitHub Actions CI workflow
docs: add CONTRIBUTING.md
test: add placeholder import test
```

---

## Phase 2 — Core Data Models

### Goal
Define the data structures that every other part of the system depends on.
Models come before everything else because they are the shared contract between
validation, storage, queue, adapters, and CLI.

### Why it exists
Writing models first prevents the rework that happens when validation and storage
are designed without knowing what they actually hold. Python `dataclasses` require
no external dependencies and produce clean, type-safe, serializable structures.

### Features
- `ContentItem` — a piece of content the user wants to repost.
- `RepostJob` — one scheduled repost attempt (content + provider).
- `RepostResult` — the recorded outcome of a completed attempt.
- `RepostStatus` — enum of all possible job/result states.
- `to_dict()` / `from_dict()` on every model (required for JSON storage in Phase 4).
- `reposting/exceptions.py` — custom exception types used across all phases.

### Files

```
[EXISTS]  reposting/__init__.py               — MODIFIED: export models in __all__

[PHASE 2] reposting/exceptions.py             — ValidationError, StorageError, AdapterError
[PHASE 2] reposting/models/__init__.py        — export all model classes
[PHASE 2] reposting/models/content.py         — ContentItem, RepostJob, RepostResult, RepostStatus
[PHASE 2] tests/test_models.py
```

### Technical design

```
ContentItem
    id:         str       — uuid4, auto-generated
    title:      str       — required
    body:       str       — required
    tags:       list[str] — optional
    created_at: datetime  — auto-set to UTC now

RepostJob
    id:           str              — uuid4
    content_id:   str              — → ContentItem.id
    provider:     str              — e.g. "mock"
    scheduled_at: datetime | None
    status:       RepostStatus
    created_at:   datetime

RepostResult
    id:           str          — uuid4
    job_id:       str          — → RepostJob.id
    provider:     str
    status:       RepostStatus
    message:      str
    attempted_at: datetime

RepostStatus (Enum)
    PENDING
    SUCCESS
    FAILED
    SKIPPED
    RETRYING   ← reserved for Phase 10 retries
```

**Serialization contract:**
- All `datetime` values stored as ISO 8601 strings in JSON.
- All enum values stored as their string name (e.g., `"SUCCESS"`).
- `to_dict()` produces a plain `dict` with only JSON-safe types.
- `from_dict(data: dict)` reconstructs the object; raises `ValueError` on missing or malformed fields.

**`exceptions.py`:**
```python
class ValidationError(Exception):
    def __init__(self, field: str, message: str): ...

class StorageError(Exception): ...

class AdapterError(Exception): ...
```

### Dependencies
- `uuid` — stdlib
- `datetime` — stdlib
- `enum` — stdlib
- `dataclasses` — stdlib

No external dependencies.

### Testing
```python
# tests/test_models.py
test_content_item_creation_with_valid_data
test_content_item_auto_generates_id
test_content_item_auto_generates_created_at
test_content_item_to_dict_produces_json_safe_types
test_content_item_from_dict_round_trip
test_content_item_from_dict_missing_field_raises_value_error
test_repost_job_creation_and_round_trip
test_repost_result_creation_and_round_trip
test_repost_status_values_are_strings_in_dict
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Implement `RepostStatus` enum | `good first issue`, `models` | Beginner | Phase 1 |
| Implement `ContentItem` dataclass | `enhancement`, `models` | Beginner | Phase 1 |
| Implement `RepostJob` dataclass | `enhancement`, `models` | Beginner | ContentItem |
| Implement `RepostResult` dataclass | `enhancement`, `models` | Beginner | RepostJob |
| Add `to_dict()` / `from_dict()` to all models | `enhancement`, `models` | Intermediate | All models |
| Add custom exception classes | `good first issue`, `models` | Beginner | Phase 1 |
| Write unit tests for all models | `testing` | Beginner | All models |

### Definition of done
- [ ] All models importable from `reposting.models`.
- [ ] All `to_dict()` / `from_dict()` round-trips verified in tests.
- [ ] `pytest tests/test_models.py` passes.
- [ ] `ruff check .` passes.
- [ ] No external dependencies added.

### Commit strategy
```
feat(exceptions): add ValidationError, StorageError, AdapterError
feat(models): add RepostStatus enum
feat(models): add ContentItem dataclass with serialization
feat(models): add RepostJob dataclass with serialization
feat(models): add RepostResult dataclass with serialization
test(models): add unit tests for all models and round-trips
```

---

## Phase 3 — Validation

### Goal
Reject invalid content at the system boundary before it ever enters the queue,
storage, or an adapter.

### Why it exists
Validation must happen at input time, not scattered across the codebase. A
dedicated validation layer means the queue, storage, and adapters can assume
the data they receive is already valid. Clear error messages with field names
make debugging fast.

### Features
- `validate_content(item: ContentItem) -> None`
  - `title`: required, 1–200 characters (strip whitespace first).
  - `body`: required, 1–5000 characters (strip whitespace first).
  - `tags`: must be a list of strings; max 10 tags; each tag ≤ 50 characters.
- Raises `ValidationError(field, message)` with the first failing rule.
- Does **not** silently coerce data — raises and lets the caller decide.

### Files

```
[PHASE 3] reposting/validation/__init__.py    — export validate_content
[PHASE 3] reposting/validation/validators.py  — all validation logic
[PHASE 3] tests/test_validation.py
```

### Technical design

```
User input
     ↓
validate_content(item: ContentItem)
     ↓ raises ValidationError(field, message)   ← on any rule violation
     ↓ returns None                              ← on success
item is safe to queue
```

Rules are expressed as a list of `(condition, field, message)` tuples evaluated
in order. Adding a new rule is a single-line change.

### Dependencies
- None (pure stdlib string operations).

### Testing
```python
# tests/test_validation.py
test_valid_item_passes
test_empty_title_raises
test_title_too_long_raises              # 201 chars
test_title_exactly_200_passes           # boundary
test_empty_body_raises
test_body_too_long_raises               # 5001 chars
test_body_exactly_5000_passes           # boundary
test_too_many_tags_raises               # 11 tags
test_exactly_10_tags_passes             # boundary
test_tag_too_long_raises                # > 50 chars
test_tags_not_a_list_raises
test_whitespace_only_title_raises
test_error_contains_field_name
test_error_contains_human_message
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Implement `validate_content()` | `enhancement`, `validation` | Beginner | Phase 2 |
| Add tag length validation | `good first issue`, `validation` | Beginner | validate_content |
| Write parametrized validation tests | `good first issue`, `testing` | Beginner | validate_content |

### Definition of done
- [ ] All rules enforced; boundary values (200, 5000, 10 tags) pass correctly.
- [ ] All error messages include the field name.
- [ ] `pytest tests/test_validation.py` passes.
- [ ] `ruff check .` passes.

### Commit strategy
```
feat(validation): implement validate_content() with all field rules
feat(validation): add whitespace stripping before validation
test(validation): add parametrized tests for all rules and boundaries
```

---

## Phase 4 — Local Storage

### Goal
Persist content items and repost history to local JSON files so the application
survives process restarts.

### Why it exists
Without persistence, every restart loses all data. The storage layer must exist
before the queue (Phase 5) and adapter (Phase 6) because both need to read and
write data. Keeping storage behind a class interface means switching from JSON
to SQLite later only requires replacing the internals of those classes.

### Features
- `config.py` — defines `DATA_DIR`, file paths, env-var override (`REPOSTING_DATA_DIR`).
- `ContentStore`:
  - `save(item: ContentItem) -> None`
  - `load(item_id: str) -> ContentItem | None`
  - `load_all() -> list[ContentItem]`
  - `delete(item_id: str) -> bool`
- `HistoryStore`:
  - `append(result: RepostResult) -> None`
  - `load_all() -> list[RepostResult]`
  - `filter(status=None, provider=None, since=None) -> list[RepostResult]`
  - `clear() -> None`
- Atomic writes: write to a temp file, then `os.replace()`. Prevents corruption on crash.
- Both stores raise `StorageError` on I/O failure.
- `DATA_DIR` is created automatically if it does not exist.

### Files

```
[PHASE 4] reposting/config.py
[PHASE 4] reposting/storage/__init__.py       — export ContentStore, HistoryStore
[PHASE 4] reposting/storage/content_store.py
[PHASE 4] reposting/storage/history_store.py
[PHASE 4] tests/conftest.py                   — shared fixtures (tmp_data_dir, etc.)
[PHASE 4] tests/test_storage.py

[RUNTIME] data/                               — git-ignored; created at runtime
[RUNTIME] data/content.json
[RUNTIME] data/history.json
[RUNTIME] data/queue.json
```

### Technical design

```
ContentStore ↔ data/content.json    (JSON array of ContentItem dicts)
HistoryStore ↔ data/history.json    (JSON array of RepostResult dicts)
RepostQueue  ↔ data/queue.json      (JSON array of RepostJob dicts — Phase 5)
```

**Atomic write pattern:**
```
write data → data/content.json.tmp
os.replace("data/content.json.tmp", "data/content.json")
```

**`config.py` pattern:**
```python
import os
from pathlib import Path

DATA_DIR     = Path(os.environ.get("REPOSTING_DATA_DIR", "data"))
CONTENT_FILE = DATA_DIR / "content.json"
HISTORY_FILE = DATA_DIR / "history.json"
QUEUE_FILE   = DATA_DIR / "queue.json"
```
The `REPOSTING_DATA_DIR` env var allows tests to redirect all I/O to a `tmp_path`.

**`conftest.py` shared fixture:**
```python
@pytest.fixture
def tmp_data_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("REPOSTING_DATA_DIR", str(tmp_path))
    # Also patch the already-imported config values
    import reposting.config as cfg
    monkeypatch.setattr(cfg, "DATA_DIR", tmp_path)
    monkeypatch.setattr(cfg, "CONTENT_FILE", tmp_path / "content.json")
    monkeypatch.setattr(cfg, "HISTORY_FILE", tmp_path / "history.json")
    monkeypatch.setattr(cfg, "QUEUE_FILE",   tmp_path / "queue.json")
    return tmp_path
```

### Dependencies
- `json` — stdlib
- `pathlib` — stdlib
- `os` — stdlib
- `tempfile` — stdlib

No external dependencies.

### Testing
```python
# tests/test_storage.py — all tests use tmp_data_dir fixture
test_content_store_save_and_load
test_content_store_load_all
test_content_store_load_nonexistent_returns_none
test_content_store_delete_existing
test_content_store_delete_nonexistent_returns_false
test_content_store_persists_across_instances
test_content_store_atomic_write
test_history_store_append_and_load_all
test_history_store_filter_by_status
test_history_store_filter_by_provider
test_history_store_filter_by_since
test_history_store_clear
test_history_store_missing_file_returns_empty_list
test_storage_raises_on_permission_error
test_data_dir_created_automatically
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Add `config.py` with `DATA_DIR` | `enhancement`, `config` | Beginner | Phase 1 |
| Implement `ContentStore` | `enhancement`, `storage` | Intermediate | Phases 2, 4 |
| Implement `HistoryStore` with filters | `enhancement`, `storage` | Intermediate | Phases 2, 4 |
| Add atomic write to storage | `enhancement`, `reliability` | Intermediate | ContentStore |
| Add `clear()` to `HistoryStore` | `good first issue`, `storage` | Beginner | HistoryStore |
| Write storage integration tests | `testing` | Intermediate | Both stores |

### Definition of done
- [ ] `ContentStore` CRUD tests pass.
- [ ] `HistoryStore` filter tests pass.
- [ ] Atomic writes verified (no partial file left on simulated crash).
- [ ] `REPOSTING_DATA_DIR` env var redirects all I/O in tests.
- [ ] No real `data/` directory created during test runs.
- [ ] `pytest tests/test_storage.py` passes.

### Commit strategy
```
feat(config): add config.py with DATA_DIR and file path constants
feat(storage): implement ContentStore with atomic JSON writes
feat(storage): implement HistoryStore with filter support
feat(storage): auto-create DATA_DIR if missing
test(storage): add conftest.py with tmp_data_dir fixture
test(storage): add storage integration tests
```

---

## Phase 5 — Repost Queue

### Goal
Manage an ordered, persistent list of repost jobs waiting to be processed.

### Why it exists
The queue is the central data structure of the application. It sits between user
intent (adding content) and execution (running an adapter). Having the queue as a
separate layer means scheduling, retries, and processing all operate on the same
ordered list without duplicating logic.

### Features
- `RepostQueue`:
  - `add(item: ContentItem) -> RepostJob` — validates, creates a `RepostJob`, persists.
  - `remove(job_id: str) -> bool`
  - `peek() -> RepostJob | None` — next job without removing.
  - `pop() -> RepostJob | None` — next job with removal.
  - `list_jobs() -> list[RepostJob]`
  - `clear() -> None`
  - `save() / load()` — JSON persistence via `config.QUEUE_FILE`.
- `add()` calls `validate_content()` — invalid items are rejected before queuing.
- Duplicate detection — same `content_id` cannot be queued twice while `PENDING`.

### Files

```
[PHASE 5] reposting/queue/__init__.py         — export RepostQueue
[PHASE 5] reposting/queue/repost_queue.py
[PHASE 5] tests/test_queue.py
```

### Technical design

```
queue.add(content_item)
         ↓
validate_content(item)        ← raises ValidationError on invalid input
         ↓
check for PENDING duplicate   ← raises if content already queued
         ↓
create RepostJob(
    content_id=item.id,
    provider="mock",           ← default; future: configurable
    status=PENDING
)
         ↓
append to internal list
         ↓
queue.save() → data/queue.json
```

### Dependencies
- Phase 2 (models), Phase 3 (validation), Phase 4 (config/storage)
- No external dependencies.

### Testing
```python
# tests/test_queue.py
test_add_valid_item_creates_pending_job
test_add_invalid_item_raises_validation_error
test_add_duplicate_pending_raises
test_remove_existing_job
test_remove_nonexistent_returns_false
test_peek_does_not_remove
test_peek_on_empty_returns_none
test_pop_removes_item
test_pop_on_empty_returns_none
test_list_jobs_returns_all
test_clear_empties_queue
test_queue_fifo_ordering
test_queue_persists_across_instances
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Implement `RepostQueue` | `enhancement`, `queue` | Intermediate | Phases 2–4 |
| Add FIFO ordering and persistence | `enhancement`, `queue` | Intermediate | RepostQueue |
| Add duplicate detection | `enhancement`, `queue`, `reliability` | Intermediate | RepostQueue |
| Add `clear()` to `RepostQueue` | `good first issue`, `queue` | Beginner | RepostQueue |
| Write queue tests | `testing` | Intermediate | RepostQueue |

### Definition of done
- [ ] FIFO ordering maintained across `save()` / `load()`.
- [ ] Invalid items rejected before entering the queue.
- [ ] Duplicate PENDING items rejected.
- [ ] All tests use `tmp_data_dir` fixture.
- [ ] `pytest tests/test_queue.py` passes.

### Commit strategy
```
feat(queue): implement RepostQueue with add, remove, peek, pop, list
feat(queue): add JSON persistence to RepostQueue
feat(queue): add duplicate PENDING content detection
feat(queue): add clear() method
test(queue): add queue operation and persistence tests
```

---

## Phase 6 — Mock Repost Adapter

### Goal
Define how repost destinations plug into the system and provide a local mock
implementation so the entire pipeline can be tested without any external service.

### Why it exists
The adapter layer is the only place that knows how to communicate with a specific
platform. Defining an abstract base class now permanently insulates the rest of
the codebase from platform-specific details. The mock adapter lets development and
CI proceed without any API credentials or network access.

### Features
- `BaseAdapter(ABC)`:
  - `name: str` — abstract property
  - `repost(job: RepostJob, item: ContentItem) -> RepostResult` — abstract method
- `MockAdapter(BaseAdapter)`:
  - `name = "mock"`
  - Constructor: `MockAdapter(fail_rate: float = 0.0, delay_ms: int = 0)`
  - Returns `RepostResult(status=SUCCESS)` or `RepostResult(status=FAILED)` based on `fail_rate`
  - Appends output to `data/mock_output.json` for manual inspection
- Adapter registry: `ADAPTERS: dict[str, type[BaseAdapter]]`

### Files

```
[PHASE 6] reposting/adapters/__init__.py      — export BaseAdapter, MockAdapter, ADAPTERS
[PHASE 6] reposting/adapters/base.py          — BaseAdapter ABC
[PHASE 6] reposting/adapters/mock_adapter.py  — MockAdapter
[PHASE 6] tests/test_adapters.py
```

### Technical design

```
BaseAdapter (ABC)
    name: str           ← abstract property
    repost(job, item)   ← abstract method → RepostResult

MockAdapter(BaseAdapter)
    name = "mock"
    repost(job, item):
        if random() < fail_rate → RepostResult(FAILED)
        else                    → RepostResult(SUCCESS)
        append to data/mock_output.json

ADAPTERS = { "mock": MockAdapter }

Usage:
    adapter = ADAPTERS[job.provider]()
    result  = adapter.repost(job, item)
```

### Dependencies
- `abc` — stdlib
- `json`, `random` — stdlib
- Phase 2 models, Phase 4 config

No external dependencies.

### Testing
```python
# tests/test_adapters.py
test_base_adapter_cannot_be_instantiated
test_mock_adapter_name_is_mock
test_mock_adapter_fail_rate_0_always_succeeds
test_mock_adapter_fail_rate_1_always_fails
test_mock_adapter_result_has_correct_job_id
test_mock_adapter_result_has_correct_provider
test_mock_adapter_writes_output_file
test_mock_adapter_output_is_valid_json
test_adapter_registry_contains_mock
test_adapter_registry_lookup_by_name
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Define `BaseAdapter` ABC | `enhancement`, `adapters` | Intermediate | Phases 2–5 |
| Implement `MockAdapter` | `enhancement`, `adapters` | Intermediate | BaseAdapter |
| Add adapter registry | `good first issue`, `adapters` | Beginner | MockAdapter |
| Write adapter tests | `testing` | Intermediate | Both |

### Definition of done
- [ ] `BaseAdapter` raises `TypeError` if instantiated directly.
- [ ] `fail_rate=0.0` always produces `SUCCESS`.
- [ ] `fail_rate=1.0` always produces `FAILED` (does not raise).
- [ ] Output file is valid JSON.
- [ ] Tests use `tmp_data_dir` and `delay_ms=0`.
- [ ] `pytest tests/test_adapters.py` passes.

### Commit strategy
```
feat(adapters): add BaseAdapter abstract base class
feat(adapters): implement MockAdapter with configurable fail rate
feat(adapters): add adapter registry
test(adapters): add adapter interface and mock behaviour tests
```

---

## Phase 7 — CLI Experience

### Goal
Wire the entire pipeline into a usable command-line interface. After this phase,
a user can add content, inspect the queue, process reposts, and view history from
the terminal. This is the phase where the project becomes genuinely usable.

### Features

| Command | Description | MVP |
|---|---|---|
| `reposting add` | Prompt for content; validate; add to queue | ✅ |
| `reposting list` | Show current queue | ✅ |
| `reposting remove <id>` | Remove a job by ID | ✅ |
| `reposting run` | Pop and repost next item via mock adapter | ✅ |
| `reposting run --all` | Run all items in queue | ✅ |
| `reposting history` | Show repost history | ✅ |
| `reposting history --status failed` | Filter history by status | ✅ |
| `reposting history --json` | Machine-readable output | ✅ |
| `reposting --version` | Show version | ✅ |
| `reposting stats` | Statistics report | Phase 9 |
| `reposting schedule` | Scheduling control | Phase 8 |

**UX principles:**
- Errors → `stderr`; exit with non-zero code.
- Empty queue → friendly message, not an error.
- IDs → show only first 8 characters in tables.
- `--json` available on all read commands.
- No external formatting libraries (pure stdlib).

### Files

```
[PHASE 7] reposting/cli/commands.py   — REWRITTEN: full subcommands replace stub
[PHASE 7] tests/test_cli.py
```

### Technical design

```
argparse (main parser)
    ├── add     → validate_content → queue.add → print confirmation
    ├── list    → queue.list_jobs → format table → stdout
    ├── remove  → queue.remove → print confirmation
    ├── run     → queue.pop → adapter.repost → history.append → print result
    └── history → history.load_all / filter → format table / JSON → stdout
```

**`commands.py` internal structure:**
```python
def main() -> None: ...         # entry point; builds parser; dispatches
def build_parser() -> ...: ...  # defines all subparsers
def cmd_add(args) -> None: ...
def cmd_list(args) -> None: ...
def cmd_remove(args) -> None: ...
def cmd_run(args) -> None: ...
def cmd_history(args) -> None: ...
```
Each `cmd_*` function is independently testable.

### Dependencies
- `argparse` — stdlib
- All previous phases

No external dependencies.

### Testing
```python
# tests/test_cli.py
test_version_flag
test_help_flag
test_add_creates_job
test_add_invalid_input_prints_to_stderr
test_list_shows_jobs
test_list_empty_queue_friendly_message
test_remove_removes_job
test_remove_nonexistent_shows_error
test_run_processes_next_job
test_run_empty_queue_friendly_message
test_run_all_processes_all_jobs
test_history_shows_results
test_history_filter_by_status
test_history_json_is_valid
```

### GitHub issues

| Title | Labels | Difficulty | Depends on |
|---|---|---|---|
| Implement `add` subcommand | `enhancement`, `cli` | Intermediate | Phases 2–5 |
| Implement `list` subcommand | `good first issue`, `cli` | Beginner | Queue |
| Implement `remove` subcommand | `good first issue`, `cli` | Beginner | Queue |
| Implement `run` subcommand | `enhancement`, `cli` | Intermediate | Phase 6 |
| Implement `history` subcommand | `enhancement`, `cli` | Intermediate | Phase 4 |
| Add `--json` to list and history | `good first issue`, `cli` | Beginner | Both |
| Write CLI integration tests | `testing` | Intermediate | All commands |

### Definition of done
- [ ] `reposting add → list → run → history` works end-to-end in the terminal.
- [ ] Invalid input exits non-zero with a message to stderr.
- [ ] Empty queue shows a friendly message (exit 0).
- [ ] `--json` produces valid JSON.
- [ ] `pytest tests/test_cli.py` passes.
- [ ] `python -m reposting --help` shows all subcommands.

### Commit strategy
```
feat(cli): implement add subcommand
feat(cli): implement list subcommand with table output
feat(cli): implement remove subcommand
feat(cli): implement run and run --all subcommands
feat(cli): implement history subcommand with filter and --json
test(cli): add CLI integration tests
```

> ↑ **Tag `v0.2.0` after this phase.** The MVP is complete.

---

## Phase 8 — Scheduling

### Goal
Allow the queue to be processed automatically on a defined schedule, without
requiring the user to manually run `reposting run`.

### Why it exists
Manual execution is fine for testing but insufficient for automation. Phase 8
comes after Phase 7 because the manual path must be stable and well-tested before
a timer is placed on top of it.

### Features
- `Scheduler`:
  - `start(interval_seconds: int) -> None`
  - `stop() -> None`
  - `status() -> dict`
- Schedule state persisted to `data/schedule.json`.
- CLI: `reposting schedule start --interval 60`, `stop`, `status`.
- Graceful shutdown on `SIGINT` / `KeyboardInterrupt`.
- If `APScheduler` is not installed: print a clear install message and exit.

### Files

```
[PHASE 8] reposting/scheduler/__init__.py     — export Scheduler
[PHASE 8] reposting/scheduler/scheduler.py
```

**Modify:**
```
[PHASE 8] reposting/cli/commands.py           — add schedule subcommand group
```

### Dependencies
- **Optional runtime**: `APScheduler>=3.10`
  - Install via: `pip install "reposting[scheduler]"`
  - Already declared in `pyproject.toml` optional extras.

### Definition of done
- [ ] `reposting schedule start --interval 10` runs queue every 10 seconds.
- [ ] Ctrl-C exits cleanly without a traceback.
- [ ] Feature degrades gracefully if APScheduler is not installed.

### Commit strategy
```
feat(scheduler): add Scheduler class with start/stop/status
feat(scheduler): integrate APScheduler as optional dependency
feat(cli): add schedule subcommand group
feat(scheduler): add SIGINT graceful shutdown
```

> ↑ **Tag `v0.3.0` after this phase.**

---

## Phase 9 — Statistics & History

### Goal
Provide meaningful insight into reposting activity using locally stored history data.

### Features
- `compute_stats(results: list[RepostResult]) -> dict`:
  - Total attempts, success count/rate, failure count/rate.
  - Breakdown per provider.
  - Reposts per day (last 7 days).
  - First and most recent timestamps.
- `reposting stats` CLI command (text + `--json`).
- `reposting history --since 7d` (filter by age).

### Files

```
[PHASE 9] reposting/stats/__init__.py         — export compute_stats
[PHASE 9] reposting/stats/stats.py
[PHASE 9] tests/test_stats.py
```

**Modify:**
```
[PHASE 9] reposting/cli/commands.py           — add stats command and --since filter
```

### Dependencies
- `collections`, `datetime` — stdlib
- No external dependencies.

### Definition of done
- [ ] `reposting stats` shows a readable, correct report.
- [ ] `--json` outputs valid JSON.
- [ ] `pytest tests/test_stats.py` passes on synthetic history data.

### Commit strategy
```
feat(stats): implement compute_stats() with per-provider breakdown
feat(cli): add stats command with --json flag
feat(cli): add --since filter to history command
test(stats): add statistics unit tests
```

---

## Phase 10 — Testing & Reliability

### Goal
Bring the test suite to production standard: coverage, integration tests across
the full pipeline, and graceful handling of all foreseeable failure modes.

### Features
- End-to-end integration test: `add → list → run → history → stats`.
- Error handling tests: corrupt JSON, missing `data/` directory, permission denied.
- Edge cases: empty queue, empty history, duplicate IDs, very long content.
- Coverage threshold raised to 90% (`fail_under = 90` in `pyproject.toml`).

### Files

```
[PHASE 10] tests/test_integration.py
```

**Modify:**
```
[PHASE 10] pyproject.toml                     — raise fail_under to 90
[PHASE 10] reposting/storage/content_store.py — add corrupt-file error handling
[PHASE 10] reposting/storage/history_store.py — add corrupt-file error handling
```

### Definition of done
- [ ] Full pipeline integration test passes.
- [ ] Corrupt JSON → `StorageError` with clear message (no raw traceback).
- [ ] `data/` missing → auto-created (already tested, double-checked here).
- [ ] Coverage ≥ 90% on `reposting/` package.
- [ ] CI green on Python 3.11 and 3.12.

---

## Phase 11 — GitHub / Open Source

### Goal
Make the project genuinely welcoming to external contributors and ready for
public visibility.

### Features
- Complete `README.md` — installation, quickstart, all CLI commands, contributing link.
- `docs/architecture.md` — pipeline diagram and module responsibility table.
- `CHANGELOG.md` — Keep-a-Changelog format.
- `SECURITY.md` — vulnerability reporting policy.
- `CODE_OF_CONDUCT.md` — Contributor Covenant.
- `.env.example` — template for future credential configuration.
- GitHub Labels, Milestones, and Discussions enabled.

### Files

```
[PHASE 11] docs/architecture.md
[PHASE 11] CHANGELOG.md
[PHASE 11] SECURITY.md
[PHASE 11] CODE_OF_CONDUCT.md
[PHASE 11] .env.example
```

**Modify:**
```
[PHASE 11] README.md           — full rewrite (first real content)
[PHASE 11] CONTRIBUTING.md     — add architecture reference
```

> ↑ **Tag `v0.4.0` after this phase.**

---

## Phase 12 — Release Preparation

### Goal
Prepare the project for a proper `v1.0.0` tag, including optional PyPI publication
and a commitment to semantic versioning stability.

### Features
- Final review of all public interfaces.
- Update `pyproject.toml` classifier: `Development Status :: 5 - Production/Stable`.
- Build and verify distribution locally.
- Publish to Test PyPI, then PyPI.

### Dependencies (dev, for building/publishing)
- `build` — `pip install build`
- `twine` — `pip install twine`

> ↑ **Tag `v1.0.0` after this phase.**

---

## Phase 13 — Future Platform Integrations

### Goal
Add real platform adapters using official APIs, slotting into the `BaseAdapter`
contract established in Phase 6.

### Design principles
- Official APIs only. No scraping. No ToS violations.
- Each adapter: `reposting/adapters/<platform>_adapter.py`.
- Credentials: environment variables only.
- Each adapter: its own optional dependency group in `pyproject.toml`.
- Adapters skipped in CI unless required env vars are present.

### Example future adapters (not planned for implementation)
- `MastodonAdapter` — Mastodon official API.
- `BlueskyAdapter` — AT Protocol.

---

## MVP Definition

### Included in MVP (v0.2.0 — Phases 1–7)

| Feature | Phase |
|---|---|
| Project structure, packaging, tooling | 1 |
| `ContentItem`, `RepostJob`, `RepostResult`, `RepostStatus` | 2 |
| `validate_content()` with all field rules | 3 |
| `ContentStore`, `HistoryStore` (JSON) | 4 |
| `config.py` with `DATA_DIR` | 4 |
| `RepostQueue` (FIFO, persistent, validated) | 5 |
| `BaseAdapter` ABC + `MockAdapter` | 6 |
| Adapter registry | 6 |
| `reposting add / list / remove / run / run --all / history` CLI | 7 |
| `--json` flag on list and history | 7 |
| CI passing on Python 3.11 and 3.12 | 1 |
| Unit tests for all modules | 1–7 |

### Excluded from MVP

| Feature | Reason |
|---|---|
| Scheduling | Adds complexity before core is stable |
| Statistics | Nice-to-have; not required for core utility |
| Real platform adapters | Require credentials, rate limits, ToS compliance |
| SQLite storage | JSON sufficient at MVP scale |
| Retry logic | Post-MVP |
| Web UI | Out of scope |
| Plugin / discovery system | Premature |
| Full documentation | Comes after functionality ships |

### What the MVP demonstrates

- ✅ Python — dataclasses, enums, ABC, argparse, pathlib, json
- ✅ Modular architecture — each concern in its own sub-package
- ✅ CLI development — argparse subcommands, stdin/stdout/stderr
- ✅ Data modelling — typed dataclasses with serialization
- ✅ Local persistence — atomic JSON reads/writes
- ✅ Error handling — custom exceptions, validation, storage errors
- ✅ Testing — unit, integration, mock, `tmp_path`, coverage
- ✅ Mock integrations — `BaseAdapter` + `MockAdapter`
- ✅ Git/GitHub workflow — branches, PRs, CI, conventional commits

---

## Architecture

### Target pipeline (full, including post-MVP)

```
User Input (CLI args / interactive prompt)
         ↓
   reposting/cli/commands.py
         ↓
   validate_content()            ← reposting/validation/
         ↓ ValidationError
         ↓
   RepostQueue.add()             ← reposting/queue/
         ↓
   queue.save()                  ← reposting/storage/  → data/queue.json
         ↓  (on `run` or scheduler tick)
   queue.pop()
         ↓
   ADAPTERS[provider]()          ← reposting/adapters/
         ↓
   adapter.repost(job, item)
         ↓
   RepostResult
         ↓
   history.append(result)        ← reposting/storage/  → data/history.json
         ↓
   compute_stats()               ← reposting/stats/
         ↓
   CLI output (stdout)
```

### Module responsibilities

| Module | Responsibility |
|---|---|
| `reposting/models/` | Pure data structures. No I/O, no business logic. |
| `reposting/exceptions.py` | Custom exception types only. |
| `reposting/validation/` | Enforce content rules. Raises; never silently coerces. |
| `reposting/config.py` | File paths and env-var overrides. Single source of truth. |
| `reposting/storage/` | Read/write JSON files. No business rules. |
| `reposting/queue/` | Manage ordered, persistent job list. Calls validation + storage. |
| `reposting/adapters/` | Platform-specific repost logic. Core never imports adapters directly. |
| `reposting/scheduler/` | Time-based queue processing. |
| `reposting/stats/` | Pure computation on history data. No I/O. |
| `reposting/cli/` | Argument parsing and output formatting. Calls domain modules. |

### Dependency rules (no circular imports)
```
cli        → queue, adapters, storage, stats, scheduler
queue      → models, validation, storage
adapters   → models, config
storage    → models, config
validation → models
stats      → models
scheduler  → queue, adapters, storage
models     → (nothing)
exceptions → (nothing)
config     → (nothing)
```

---

## Data Design

### ContentItem
```
id:          str          — uuid4, auto-generated on creation
title:       str          — required, 1–200 chars
body:        str          — required, 1–5000 chars
tags:        list[str]    — optional, max 10, each ≤ 50 chars
created_at:  datetime     — auto-set to UTC now
```

### RepostJob
```
id:           str              — uuid4
content_id:   str              — → ContentItem.id
provider:     str              — "mock" or future platform name
scheduled_at: datetime | None  — None = process immediately
status:       RepostStatus
created_at:   datetime
```

### RepostResult
```
id:           str           — uuid4
job_id:       str           — → RepostJob.id
provider:     str
status:       RepostStatus  — SUCCESS, FAILED, SKIPPED
message:      str           — human-readable outcome
attempted_at: datetime
```

### RepostStatus (Enum)
```
PENDING    — in the queue, not yet processed
SUCCESS    — completed successfully
FAILED     — attempted but failed
SKIPPED    — removed before processing
RETRYING   — reserved for Phase 10 retry logic
```

### Relationships
```
ContentItem  1──< M  RepostJob  1──1  RepostResult
```
One content item can have multiple jobs (reposted multiple times).
One job produces exactly one result when completed.

---

## CLI Design

### MVP commands

```bash
reposting add
reposting add --title "Title" --body "Body" --tags "tag1,tag2"

reposting list
reposting list --json

reposting remove <job-id>

reposting run
reposting run --all
reposting run --provider mock

reposting history
reposting history --status failed
reposting history --json

reposting --version
reposting --help
```

### Post-MVP commands

```bash
reposting stats
reposting stats --json

reposting history --since 7d

reposting schedule start --interval 60
reposting schedule stop
reposting schedule status
```

### UX principles
- Errors → `sys.stderr`; `sys.exit(1)`.
- Friendly empty states → `sys.stdout`; `sys.exit(0)`.
- IDs → display first 8 characters in tables.
- `--json` on all read commands.
- No third-party formatting libraries.

---

## Storage Design

### JSON (recommended for MVP)

**Pros:** Zero dependencies; human-readable; easy to debug; simple `tmp_path` testing.
**Cons:** Full-file rewrite on every write; no indexing; concurrency-unsafe.

### SQLite (post-MVP consideration)

**Pros:** Efficient queries; transactional; concurrent read support; stdlib `sqlite3`.
**Cons:** More complex; requires schema migrations; harder to manually inspect.

### Recommendation
Use **JSON for the MVP**. The storage layer is already behind `ContentStore` and
`HistoryStore` interfaces, so migrating to SQLite later only requires replacing
the internals of those two classes — no other code changes.

**Migration trigger:** Switch to SQLite when history exceeds ~10,000 entries or
when concurrent scheduler + CLI access causes race conditions.

---

## Testing Architecture

```
tests/
├── __init__.py              — makes tests/ a package
├── conftest.py              — shared fixtures (tmp_data_dir, sample items)
├── test_models.py           — ContentItem, RepostJob, RepostResult, RepostStatus
├── test_validation.py       — validate_content() and all rules
├── test_storage.py          — ContentStore, HistoryStore
├── test_queue.py            — RepostQueue operations and persistence
├── test_adapters.py         — BaseAdapter ABC, MockAdapter
├── test_cli.py              — all CLI subcommands
├── test_stats.py            — compute_stats() (Phase 9)
└── test_integration.py      — end-to-end pipeline (Phase 10)
```

### Testing rules
1. Never write to real `data/` — always use `tmp_data_dir` fixture.
2. No network calls in tests — mock adapter only.
3. No `time.sleep` — inject `delay_ms=0` into MockAdapter.
4. Use `pytest.raises` for all expected exceptions.
5. Coverage ≥ 80% from Phase 7; ≥ 90% from Phase 10.
6. All tests run on Python 3.11 and 3.12 in CI.

---

## GitHub / Open-Source Strategy

### Labels

| Label | Purpose |
|---|---|
| `good first issue` | Small, well-defined tasks for new contributors |
| `enhancement` | New features |
| `bug` | Something is broken |
| `documentation` | README, docstrings, guides |
| `testing` | Adding or improving tests |
| `models` | Data model changes |
| `validation` | Validation rules |
| `storage` | Persistence layer |
| `queue` | Queue operations |
| `adapters` | Adapter interface and implementations |
| `cli` | CLI commands and UX |
| `scheduler` | Scheduling |
| `stats` | Statistics and history |
| `reliability` | Error handling, atomicity |
| `ci` | GitHub Actions, tooling |
| `refactor` | Code quality |
| `wontfix` | Explicitly out of scope |

### Milestones

| Milestone | Phases | Version |
|---|---|---|
| Foundation | 0–1 | v0.1.0 |
| Core functionality (MVP) | 2–7 | v0.2.0 |
| Scheduling & statistics | 8–9 | v0.3.0 |
| Reliability & contributor improvements | 10–11 | v0.4.0 |
| Stable release | 12 | v1.0.0 |

### Branch strategy
```
main          ← always releasable; protected
feat/<name>   ← new features
fix/<name>    ← bug fixes
docs/<name>   ← documentation only
chore/<name>  ← tooling, config
```

### Contributor tiers

**Beginner (`good first issue`):**
- Add `clear()` to `HistoryStore`
- Add `clear()` to `RepostQueue`
- Add `--json` flag to `list` command
- Add tag count validation
- Add missing docstrings
- Add `CHANGELOG.md`
- Add `SECURITY.md`

**Intermediate:**
- Implement `ContentStore`
- Implement `HistoryStore` filters
- Implement `RepostQueue` persistence
- Add storage integration tests
- Implement `stats` command

**Advanced:**
- Implement `MockAdapter` with fail rate
- Implement full integration test suite
- Implement `Scheduler` with APScheduler
- Design SQLite migration path
- Implement a real platform adapter (post-v1.0.0)

---

## Release Roadmap

### v0.1.0 — Foundation
**Includes:** Phase 1 — project structure, packaging, CLI stub, CI.
**Does not do:** Any functional reposting.
**Criteria:** CI green; `python -m reposting --version` works; package installable.

### v0.2.0 — Core Functionality (MVP)
**Includes:** Phases 2–7 — full pipeline.
**Does not do:** Scheduling, statistics, real adapters.
**Criteria:** `add → list → run → history` end-to-end; tests pass; coverage ≥ 80%.

### v0.3.0 — Scheduling & Statistics
**Includes:** Phases 8–9.
**Criteria:** `schedule start --interval N` works; `stats` shows correct output.

### v0.4.0 — Reliability & Contributor Improvements
**Includes:** Phases 10–11.
**Criteria:** Coverage ≥ 90%; full README; architecture docs; contributor infrastructure.

### v1.0.0 — Stable Release
**Includes:** Phase 12 — reviewed API, PyPI publication.
**Criteria:** All interfaces stable; published to PyPI; no known bugs.

> [!CAUTION]
> Do not tag `v1.0.0` until all public interfaces are reviewed and intentionally stable.
> A premature `v1.0.0` creates false expectations about backwards compatibility.

---

## Security & Reliability

| Risk | Impact | Mitigation |
|---|---|---|
| Credentials in source code | Security breach | Env vars only; `.env` git-ignored; `.env.example` template |
| Malformed input | Crash or bad data | `validate_content()` at every entry point; `from_dict()` raises on bad data |
| Corrupt JSON files | Data loss | Atomic writes (temp → rename); catch `json.JSONDecodeError` → `StorageError` |
| Duplicate reposts | Same content posted twice | PENDING duplicate check in `queue.add()` |
| Failed reposts | Silent data loss | `RepostResult(FAILED)` always written; never swallow exceptions |
| Missing `data/` directory | `FileNotFoundError` | `config.py` creates `DATA_DIR` automatically |
| Permission errors on `data/` | StorageError crash | Catch `PermissionError`; wrap in `StorageError` with a clear message |
| Scheduling failures | Missed runs | Persist next-run time; detect and catch up on restart |
| Rate limits (future adapters) | API ban | Adapter layer handles rate-limit state; exponential back-off |
| External API changes | Broken adapters | Only adapter code changes; core is insulated |
| Platform restrictions | ToS violation | Official APIs only; documented in CONTRIBUTING.md |
| Python version drift | Incompatibility | `.python-version` pins 3.11; CI tests 3.11 and 3.12 |

---

## Final Implementation Order

```
Phase 0  — Confirm baseline
         ├── Confirm only README.md, main.py, implementation_plan.md exist
         └── Gate: working tree clean; no extra files

Phase 1  — Project Foundation
         ├── Add .gitignore, .python-version, LICENSE
         ├── Add pyproject.toml
         ├── Create reposting/ package skeleton
         ├── Update main.py to thin shim
         ├── Add CONTRIBUTING.md
         ├── Add .github/ CI, issue templates, PR template
         ├── Add tests/__init__.py + placeholder import test
         └── Gate: pytest passes; ruff clean; CI green; --version works
                    TAG v0.1.0

Phase 2  — Core Data Models
         ├── Create reposting/exceptions.py
         ├── Create reposting/models/ (all models + serialization)
         ├── Create tests/test_models.py
         └── Gate: all round-trips pass; ruff clean

Phase 3  — Validation
         ├── Create reposting/validation/
         ├── Create tests/test_validation.py
         └── Gate: all rules + boundaries tested

Phase 4  — Local Storage
         ├── Create reposting/config.py
         ├── Create reposting/storage/ (ContentStore, HistoryStore)
         ├── Create tests/conftest.py
         ├── Create tests/test_storage.py
         └── Gate: round-trips pass; tmp_data_dir used; no real data/ created

Phase 5  — Repost Queue
         ├── Create reposting/queue/
         ├── Create tests/test_queue.py
         └── Gate: FIFO ordering + persistence + duplicate detection verified

Phase 6  — Mock Adapter
         ├── Create reposting/adapters/ (BaseAdapter, MockAdapter, registry)
         ├── Create tests/test_adapters.py
         └── Gate: fail_rate=0.0 always SUCCESS; fail_rate=1.0 always FAILED

Phase 7  — CLI
         ├── Rewrite reposting/cli/commands.py (full subcommands)
         ├── Create tests/test_cli.py
         └── Gate: add → list → run → history works end-to-end in terminal
                    TAG v0.2.0  ← MVP complete

Phase 8  — Scheduling
         ├── Create reposting/scheduler/
         ├── Modify cli/commands.py (schedule subcommands)
         └── Gate: 10-second interval run works; Ctrl-C exits cleanly
                    TAG v0.3.0

Phase 9  — Statistics & History
         ├── Create reposting/stats/
         ├── Modify cli/commands.py (stats, --since)
         ├── Create tests/test_stats.py
         └── Gate: stats correct on synthetic data

Phase 10 — Testing & Reliability
         ├── Create tests/test_integration.py
         ├── Add corrupt-file handling to storage
         └── Gate: coverage ≥ 90%; integration test passes; CI green

Phase 11 — GitHub / Open Source
         ├── Rewrite README.md
         ├── Create docs/architecture.md
         ├── Create CHANGELOG.md, SECURITY.md, CODE_OF_CONDUCT.md, .env.example
         └── Gate: README quickstart tested manually; all links resolve
                    TAG v0.4.0

Phase 12 — Release Preparation
         ├── Review and lock public interfaces
         ├── Update pyproject.toml classifiers
         ├── Build and verify distribution
         └── Gate: pip install reposting from PyPI works
                    TAG v1.0.0

Phase 13 — Future Platform Integrations
         ← Only after v1.0.0 is shipped and stable
```

---

*Plan written on 2026-09-17. Starting point: 3 files (README.md, main.py, implementation_plan.md).*
*No code changes have been made. Awaiting approval before implementation begins.*
