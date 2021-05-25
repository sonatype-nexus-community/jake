#!/usr/bin/env bash
set -e

# intended to be run from directory above this one.

# Setup a proper path, I call my virtualenv dir ".venv_non_dev"
PATH=$WORKSPACE/.venv_non_dev/bin:$PATH
python3 --version
if [ ! -d ".venv_non_dev" ]; then
        # use python3 to create .venv
        python3 -m venv .venv_non_dev
fi
source .venv_non_dev/bin/activate
#pip3 install pipenv

pip3 install python-semantic-release

pip3 install -r requirements.txt

# Setup a proper path, I call my virtualenv dir ".venv_dev"
PATH=$WORKSPACE/.venv_dev/bin:$PATH
python3 --version
if [ ! -d ".venv_dev" ]; then
        # use python3 to create .venv
        python3 -m venv .venv_dev
fi
source .venv_dev/bin/activate
#pip3 install pipenv

pip3 install python-semantic-release

pip3 install -r requirements.txt

# development only requirements
pip3 install -r requirements-dev.txt
