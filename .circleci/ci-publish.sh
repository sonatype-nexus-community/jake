#!/usr/bin/env bash

source .venv/bin/activate

# Configure GIT with host fingerprint, user info and SSH key for pushing
mkdir -p ~/.ssh
echo "Adding github.com as known host..."
echo $GITHUB_FINGERPRINT >> ~/.ssh/known_hosts
echo "Setting private SSH key for pushing new version to repo..."
echo $GITHUB_COMMIT_KEY | base64 --decode >> ~/.ssh/id_rsa
chmod 400 ~/.ssh/id_rsa # prevents "UNPROTECTED PRIVATE KEY FILE" error
git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_EMAIL"

semantic-release version --patch

# semantic-release publish
