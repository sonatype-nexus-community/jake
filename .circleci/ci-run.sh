#!/usr/bin/env bash

source .venv/bin/activate

pip install flake8

flake8 jake

python3 -m unittest discover
