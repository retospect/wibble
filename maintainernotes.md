# Maintainer's build notes

Publishing uses [trusted publishing](https://docs.pypi.org/trusted-publishers/) via GitHub Actions — no API tokens needed.

## Release workflow

```bash
git clean -fdx --dry-run
uv run ruff check .
uv run pytest
git commit -am "prep release"
bump-my-version bump patch   # or: minor / major
git push && git push --tags
```

Then create a **GitHub Release** from the tag — the CI workflow builds and publishes to PyPI automatically.

## Local testing

```bash
uv build
uv pip install --force-reinstall dist/*.whl
fafa
```
