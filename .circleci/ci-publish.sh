#!/usr/bin/env bash

source .venv/bin/activate

semantic-release version --patch

# semantic-release publish