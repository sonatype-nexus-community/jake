#!/usr/bin/env bash

source .venv/bin/activate

pip install pylint

pylint .

python3 -m unittest discover
