#!/usr/bin/env bash

source .venv/bin/activate

pip install pylint

pylint jake

python3 -m unittest discover
