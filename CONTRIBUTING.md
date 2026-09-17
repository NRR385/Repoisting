# Contributing to Reposting

Thank you for your interest in contributing! This guide explains how to get started.

---

## Code of Conduct

Please be respectful and constructive. We follow the spirit of the
[Contributor Covenant](https://www.contributor-covenant.org/).

---

## Getting started

### 1. Fork and clone the repository

```bash
git clone https://github.com/NRR385/Reposting.git
cd Reposting
```

### 2. Set up a virtual environment

```bash
python -m venv .venv

# Activate:
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 3. Install development dependencies

```bash
pip install -e ".[dev]"
```

### 4. Verify the setup

```bash
python -m reposting --version   # should print: reposting 0.1.0
pytest                          # all tests should pass
ruff check .                    # should report zero issues
```

---

## Development workflow

### Branching

- Branch off `main` for every change.
- Use a descriptive branch name, e.g. `feat/queue-persistence` or `fix/validation-edge-case`.

### Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

Examples:
  feat(queue): add JSON persistence to RepostQueue
  fix(validation): handle empty tag list correctly
  test(history): add filter-by-status tests
  docs(readme): update installation instructions
  chore(ci): add Python 3.12 to CI matrix
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`, `build`.

### Code style

We use [ruff](https://docs.astral.sh/ruff/) for linting and formatting:

```bash
ruff check .            # lint
ruff format .           # auto-format
ruff check --fix .      # auto-fix safe issues
```

All PRs must pass `ruff check .` and `ruff format --check .`.

### Running tests

```bash
pytest                          # run all tests
pytest tests/test_queue.py      # run a specific file
pytest --cov=reposting          # with coverage report
```

Tests live in `tests/`. Every new feature or bug fix should include a corresponding test.

---

## Finding something to work on

Look for issues labelled [`good first issue`](https://github.com/NRR385/Reposting/labels/good%20first%20issue) — these are small, well-scoped tasks suitable for new contributors.

If you want to work on something, comment on the issue first so we can avoid duplicate effort.

---

## Submitting a pull request

1. Push your branch to your fork.
2. Open a PR against `main` on this repository.
3. Fill in the PR template completely.
4. Ensure CI passes (lint + tests).
5. Request a review.

Keep PRs small and focused — one feature or fix per PR.

---

## Project structure

```
reposting/          Installable Python package
tests/              Test suite (pytest)
.github/            CI workflows and issue/PR templates
pyproject.toml      Packaging and tool configuration
CONTRIBUTING.md     This file
```

For a full architectural overview, see [docs/architecture.md](docs/architecture.md) (added in Phase 10).

---

## Questions

Open a [GitHub Discussion](https://github.com/NRR385/Reposting/discussions) or file an issue.
