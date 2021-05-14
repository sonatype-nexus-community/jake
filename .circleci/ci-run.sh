#!/usr/bin/env bash
set -e

source .venv_dev/bin/activate
#pipenv shell

pylint jake

#python3 -m unittest discover
python -m xmlrunner discover -o test-results/
