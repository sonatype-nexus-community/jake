#!/usr/bin/env bash

git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_EMAIL"

semantic-release version --patch

# semantic-release publish