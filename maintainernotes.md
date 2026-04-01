# Maintainer's build notes

Publishing uses [trusted publishing](https://docs.pypi.org/trusted-publishers/) via GitHub Actions — no API tokens needed.

## Release workflow

```bash
git clean -fdx --dry-run
uv run ruff check .
uv run pytest
uv version 1.2.3              # set the new version (single source of truth)
git commit -am "release 1.2.3"
git tag v1.2.3
git push && git push --tags
```

Then create a **GitHub Release** from the tag — the CI workflow builds and publishes to PyPI automatically.

Version lives only in `pyproject.toml`. `__init__.py` reads it at runtime via `importlib.metadata`.

## Local testing

```bash
uv build
uv pip install --force-reinstall dist/*.whl
fafa
```
