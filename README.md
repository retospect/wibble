[![check](https://github.com/retospect/wibble/actions/workflows/check.yml/badge.svg)](https://github.com/retospect/wibble/actions/workflows/check.yml)

# Wibble — a template for simple python packages

A minimalist template for a Python package using modern tooling:
**hatchling** build backend, **uv** for dependency management, **ruff** for linting/formatting, **GitHub Actions** CI with trusted PyPI publishing.

## Quick start

```bash
uv run pre-commit install  # set up git hooks (once)
uv run pytest              # run tests
uv run ruff check .        # lint
uv run ruff format .       # format
uv run mypy src tests      # type check
uv run fafa                # run the CLI entry point
```

## Things to replace

- `grep -ri word .` will find *word* in all files
- `find . | grep word` will find *word* in any filenames
- **retospect** — change to your GitHub username
- **wibble** — change to the name of your project
- **wobble** — change to the internal module name
- **fafa** — change to your CLI command name
- Update `pyproject.toml` with your name, description, and URLs

## Security practices

- All GitHub Actions **pinned by commit SHA** to prevent supply chain attacks
- PyPI publishing via **trusted publishing** (OIDC) — no long-lived API tokens
- **Build provenance attestations** on every release ([actions/attest-build-provenance](https://github.com/actions/attest-build-provenance))
- **Dependabot** monitors pip + GitHub Actions dependencies weekly; minor/patch PRs auto-merged after CI passes
- **Least-privilege permissions** — workflows default to `contents: read`
- See [SECURITY.md](SECURITY.md) for the vulnerability disclosure policy
