# Maintainer's build notes

```
git commit 
git clean -fdx --dry-run
tox
bumpver update --patch
flit build
flit publish

```
gpg sign soon!

## test:
```
pip uninstall -y wibble
python -m pip cache purge

pip install wibble
```
