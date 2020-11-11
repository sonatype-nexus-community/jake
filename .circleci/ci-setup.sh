#!/usr/bin/env bash
set -e

# intended to be run from directory above this one.

# Setup a proper path, I call my virtualenv dir ".venv"
PATH=$WORKSPACE/.venv/bin:$PATH
python3 --version
if [ ! -d ".venv" ]; then
        # use python3 to create .venv
        python3 -m venv .venv
fi
source .venv/bin/activate
#pip3 install pipenv

pip3 install python-semantic-release

pip3 install -r requirements.txt

# development only requirements
pip3 install -r requirements-dev.txt
