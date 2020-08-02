#!/usr/bin/env bash

bumpversion $1
python3 setup.py sdist bdist_wheel
twine upload dist/*.tar.gz
rm -rf build
rm -rf dist
rm -rf cqcli.egg-info
