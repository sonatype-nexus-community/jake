#!/usr/bin/env bash

source .venv/bin/activate

pip install pylint

pylint jake --ignore=test/

python3 -m unittest discover
