#!/usr/bin/env bash
set -e

# intended to be run from directory above this one.

# Setup a proper path, I call my virtualenv dir ".venv_self_scan"
PATH=$WORKSPACE/.venv_self_scan/bin:$PATH
python3 --version
if [ ! -d ".venv_self_scan" ]; then
        # use python3 to create .venv
        python3 -m venv .venv_self_scan
fi
source .venv_self_scan/bin/activate
#pip3 install pipenv

pip3 install python-semantic-release

pip3 install -r requirements.txt

# Setup a proper path, I call my virtualenv dir ".venv_test"
PATH=$WORKSPACE/.venv_test/bin:$PATH
python3 --version
if [ ! -d ".venv_test" ]; then
        # use python3 to create .venv
        python3 -m venv .venv_test
fi
source .venv_test/bin/activate
#pip3 install pipenv

pip3 install python-semantic-release

pip3 install -r requirements.txt

# development only requirements
pip3 install -r requirements-dev.txt
