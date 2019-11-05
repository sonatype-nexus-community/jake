#!/usr/bin/env bash

# Configure GIT with user info for pushing
git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_EMAIL"

semantic-release publish --patch
