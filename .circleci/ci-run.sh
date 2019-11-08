#!/usr/bin/env bash
set -e

source .venv/bin/activate

pylint jake

python3 -m unittest discover
