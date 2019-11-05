#!/usr/bin/env bash

git config --global user.name "semantic-release (via CircleCI)"
git config --global user.email "semantic-release@circle"

semantic-release version --patch

# semantic-release publish