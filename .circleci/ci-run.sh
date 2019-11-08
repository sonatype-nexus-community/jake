#!/usr/bin/env bash

source .venv/bin/activate

pylint jake

LINTER_STATUS=$?
echo "LINTER_STATUS: $LINTER_STATUS"
if [ $LINTER_STATUS -ne 0 ]; then
  echo "failed linter status: $status"
  exit 1
fi

python3 -m unittest discover
