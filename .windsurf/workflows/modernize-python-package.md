---
description: Migrate a Python package to modern best practices (hatchling + uv + ruff)
---

Modernize this Python package to current best practices. Use retospect/wibble v1.0.0 as the reference template. Here is the target state:

## Build & Packaging
- **Build backend**: `hatchling` — replace poetry-core, setuptools, flit, or whatever is currently used
- **Metadata**: PEP 621 `[project]` table in `pyproject.toml` — not `[tool.poetry]` or `setup.cfg`
- **License**: SPDX identifier in `license` field (e.g. `"GPL-3.0-only"`, `"MIT"`)
- **Python**: `requires-python = ">=3.11"`, classifiers for 3.11/3.12/3.13
- **Version**: single source of truth in `pyproject.toml`. `__init__.py` uses `from importlib.metadata import version; __version__ = version("pkg")`. No version duplication anywhere.
- **py.typed**: add empty `src/<pkg>/py.typed` marker (PEP 561)

## Dependencies & Dev Tools
- **Dev deps**: PEP 735 `[dependency-groups]` with: `pytest>=8`, `ruff>=0.11`, `mypy>=1.15`, `pre-commit>=4`
- **Delete**: `tox.ini`, `setup.cfg`, `setup.py`, `poetry.lock`, `.flake8`, `.isort.cfg`, `MANIFEST.in` if present. Remove `bumpver`/`bump2version`/`bump-my-version` config and deps.
- **Keep**: `uv.lock` committed (not gitignored)

## Tool Config (all in pyproject.toml)
- **ruff**: `target-version = "py311"`, `line-length = 88`, select `["E", "F", "I", "UP", "B", "SIM", "RUF"]`
- **mypy**: `python_version = "3.11"`, `warn_return_any = true`, `warn_unused_configs = true`, `check_untyped_defs = true`
- **pytest**: `testpaths = ["tests"]`

## Pre-commit (.pre-commit-config.yaml)
- `ruff-pre-commit`: ruff (with --fix) + ruff-format hooks
- `pre-commit-hooks`: trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files

## CI (.github/workflows/check.yml)
- **All actions pinned by commit SHA** with version comment (e.g. `actions/checkout@<sha> # v4.3.1`)
- **Top-level** `permissions: contents: read`
- **lint job**: ruff check, ruff format --check, mypy
- **test job**: matrix of ubuntu/macos/windows × python 3.11/3.12/3.13, runs `uv run pytest`
- **publish job**: needs lint+test, triggers on tags, uses `environment: pypi`, permissions `id-token: write` + `attestations: write`, runs `uv build`, `actions/attest-build-provenance`, `pypa/gh-action-pypi-publish`
- Use `astral-sh/setup-uv` (latest SHA-pinned)

## Dependabot (.github/dependabot.yml)
- pip + github-actions ecosystems, weekly
- Commit-message prefixes: `deps` for pip, `ci` for actions
- Group minor+patch pip updates; group all actions updates
- Separate `dependabot-auto-merge.yml` workflow: auto-squash-merge non-major dependabot PRs using `dependabot/fetch-metadata` (SHA-pinned)

## Security
- `SECURITY.md` with private vulnerability reporting via GitHub advisories
- `.gitignore`: only build/tool artifacts (`__pycache__/`, `*.py[cod]`, `*.egg-info/`, `dist/`, `build/`, `.mypy_cache/`, `.ruff_cache/`, `.pytest_cache/`, `.venv/`)

## Process
1. Read existing pyproject.toml/setup.cfg/setup.py to understand current deps, entry points, metadata
2. Rewrite pyproject.toml from scratch in the target format, preserving all real dependencies and entry points
3. Delete obsolete files (tox.ini, setup.cfg, setup.py, .flake8, etc.)
4. Update __init__.py to use importlib.metadata
5. Add py.typed marker
6. Create/replace .pre-commit-config.yaml
7. Create/replace .github/workflows/check.yml
8. Create/replace .github/workflows/dependabot-auto-merge.yml
9. Create/replace .github/dependabot.yml
10. Create SECURITY.md if missing
11. Update .gitignore
12. Update README.md with quick-start and security-practices sections
13. Run `uv run ruff check --fix .` then `uv run ruff format .` to fix existing code
14. Run `uv run mypy src tests` and fix any errors
15. Run `uv run pytest` and confirm all tests pass
16. Commit and push
