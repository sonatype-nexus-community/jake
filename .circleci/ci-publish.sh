#!/usr/bin/env bash
set -e

python3 -m venv .venv

source .venv_non_dev/bin/activate

pip3 install -r requirements.txt

pip3 install python-semantic-release

pip3 install --upgrade setuptools twine wheel

git config user.name "$GITHUB_USERNAME"

git config user.email "$GITHUB_EMAIL"

semantic-release publish --patch
