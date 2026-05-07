#
# Copyright 2019-Present Sonatype Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

## How to be a contributor to this project

### Are you submitting a pull request?

* Make sure to fill out an issue for your PR, so that we have traceability as to what you are trying to fix,
  versus how you fixed it.
* Sign the [Sonatype CLA](https://sonatypecla.herokuapp.com/sign-cla)
* Sign your commits: `git commit -S -s` — this is required to satisfy the
  [Developer Certificate of Origin](https://developercertificate.org/)
* Try to fix one thing per pull request! Many people work on this code, so the more focused your changes are, the less
  of a headache other people will have when they merge their work in.
* Ensure your Pull Request passes all CI checks (linting, static analysis, tests)
* Add yourself or your organization to `.github/CONTRIBUTORS.md` as part of your PR if you are new to the project!

### Development Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management and
[tox](https://tox.wiki/) to orchestrate testing.

```shell
# Install Poetry
pip install poetry

# Install all dependencies
poetry install

# Run linting
poetry run tox -e flake8

# Run static analysis
poetry run tox -e mypy-locked

# Run tests
poetry run tox -e py310-locked
```

### Coding Standards

* Python code is linted with `flake8` (max line length 120)
* Static typing is checked with `mypy`
* All new code must have corresponding tests

### Are you new and looking to dive in?

* Check [open issues](https://github.com/sonatype-nexus-community/jake/issues) to see if there is something you can
  help with.
* Join the [Sonatype Community](https://community.sonatype.com/) for discussions and help.
