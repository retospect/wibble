# Maintainer's build notes

How to [set up to publish a package](https://towardsdatascience.com/how-to-publish-a-python-package-to-pypi-using-poetry-aa804533fc6f).

```
git clean -fdx --dry-run
tox
git commit 
bumpver update --patch
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```

gpg sign soon!

## test:
```
pip uninstall -y wibble
python -m pip cache purge

pip install wibble

pip install --force-reinstall dist/*.whl
```
