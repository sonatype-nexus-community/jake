#!/usr/bin/env bash
set -e

source .venv/bin/activate

pylint jake

#python3 -m unittest discover
# us nose to write test ouput to junit compatible file for use in CI
mkdir -p test-results
nosetests --with-xunit --xunit-file=test-results/nosetests.xml --with-coverage --cover-xml --cover-xml-file=test-results/coverage.xml
