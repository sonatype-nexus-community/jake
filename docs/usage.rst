.. #
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

Usage
====================================================

Getting Started
---------------

``jake`` can guide you...

.. code-block::

    > jake --help
    usage: jake [-h] [-v] [-w] [-X]  ...

    Put your Python dependencies in a chokehold

    options:
      -h, --help       show this help message and exit
      -v, --version    show which version of jake you are running
      -w, --warn-only  prevents exit with non-zero code when issues have been
                       detected
      -X               enable debug output

    Jake sub-commands:

        guide          perform a scan backed by Sonatype Guide
        ddt            (DEPRECATED: use guide instead) perform a scan backed by Sonatype Guide
        iq             perform a scan backed by Sonatype Lifecycle
        sbom           generate a CycloneDX software-bill-of-materials (no
                       vulnerabilities)


``jake`` will exit with code ``0`` under normal operation and ``1`` if vulnerabilities are found (Sonatype Guide) or
Policy Violations are detected (Sonatype Lifecycle), unless you pass the ``-w`` flag in which case ``jake`` will always
exit with code ``0``.

Generating an SBOM
------------------

``jake`` can take data from various inputs (or just look at your current Python environment) and produce a CycloneDX
for you.

.. code-block::

    > jake sbom --help

    usage: jake sbom [-h] [-f FILE_PATH] [-t TYPE] [-o PATH/TO/FILE]
                       [--output-format {json,xml}]
                       [--schema-version {1.0,1.1,1.2,1.3,1.4,1.5,1.6}]

    options:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is
                            not specified directly here, then we will attempt to
                            read data from STDIN. If there is no data on STDIN, we
                            will then fall back to looking for standard files in
                            the current directory that relate to the type of input
                            indicated by the -t flag.
      -t TYPE, --type TYPE, -it TYPE, --input-type TYPE
                            how jake should find the packages from which to
                            generate your SBOM. ENV = Read from the current Python
                            Environment; CONDA = Read output from `conda list
                            --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV =
                            read from Pipfile.lock; POETRY = read from a
                            poetry.lock. (Default = ENV)
      -o PATH/TO/FILE, --output-file PATH/TO/FILE
                            Specify a file to output the SBOM to
      --output-format {json,xml}
                            SBOM output format (default = xml)
      --schema-version {1.0,1.1,1.2,1.3,1.4,1.5,1.6}
                            CycloneDX schema version to use (default = 1.6)

Check out these examples using STDIN:

.. code-block::

    conda list --explicit --md5 | jake sbom -t CONDA
    conda list --json | jake sbom -t CONDA_JSON
    cat /path/to/Pipfile.lock | jake sbom -t PIPENV


Check out these examples specifying a manifest:

.. code-block::

    jake sbom -t PIP -f /path/to/requirements.txt
    jake sbom -t PIPENV -f /path/to/Pipfile.lock


Check for vulnerabilities using Sonatype Guide
----------------------------------------------

``jake`` will look at the packages installed in your current Python environment and check these against
`Sonatype Guide`_ for you. Optionally, it can create a CycloneDX software bill-of-materials at the same time.

Authentication
~~~~~~~~~~~~~~

Sonatype Guide requires a registered account. Sign up at `guide.sonatype.com`_ and generate an API token.
Supply your credentials via environment variables (recommended) or CLI flags:

.. list-table::
   :header-rows: 1

   * - Variable
     - Purpose
   * - ``SONATYPE_GUIDE_USERNAME``
     - Your Sonatype Guide username / email
   * - ``SONATYPE_GUIDE_TOKEN``
     - Your Sonatype Guide API token

.. code-block::

    > jake guide --help

    usage: jake guide [-h] [-f FILE_PATH] [-t TYPE] [-u USERNAME] [--token TOKEN]
                      [-o PATH/TO/FILE] [--output-format {json,xml}]
                      [--schema-version {1.0,1.1,1.2,1.3,1.4,1.5,1.6}]
                      [--whitelist PATH]

    options:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is
                            not specified directly here, then we will attempt to
                            read data from STDIN. If there is no data on STDIN, we
                            will then fall back to looking for standard files in
                            the current directory that relate to the type of input
                            indicated by the -t flag.
      -t TYPE, --type TYPE, -it TYPE, --input-type TYPE
                            how jake should find the packages from which to
                            generate your SBOM. ENV = Read from the current Python
                            Environment; CONDA = Read output from `conda list
                            --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV =
                            read from Pipfile.lock; POETRY = read from a
                            poetry.lock. (Default = ENV)
      -u USERNAME, --username USERNAME
                            Sonatype Guide username/email
                            (env var: SONATYPE_GUIDE_USERNAME)
      --token TOKEN         Sonatype Guide API token
                            (env var: SONATYPE_GUIDE_TOKEN)
      -o PATH/TO/FILE, --output-file PATH/TO/FILE
                            Specify a file to output the SBOM to. If not specified
                            the report will be output to the console.
                            STDOUT is not supported.
      --output-format {json,xml}
                            SBOM output format (default = xml)
      --schema-version {1.0,1.1,1.2,1.3,1.4,1.5,1.6}
                            CycloneDX schema version to use (default = 1.6)
      --whitelist PATH      Set path to whitelist json file

So you can quickly get a report by running:

.. code-block::

    > export SONATYPE_GUIDE_USERNAME=your@email.com
    > export SONATYPE_GUIDE_TOKEN=your-api-token
    > jake guide

Check out these examples using STDIN:

.. code-block::

    conda list --explicit --md5 | jake guide -t CONDA
    conda list --json | jake guide -t CONDA_JSON
    cat /path/to/Pipfile.lock | jake guide -t PIPENV


Check out these examples specifying a manifest:

.. code-block::

    jake guide -t PIP -f /path/to/requirements.txt
    jake guide -t PIPENV -f /path/to/Pipfile.lock


Pre-commit Hook
~~~~~~~~~~~~~~~

A pre-commit hook is also available for use:

.. code-block:: yaml

  - repo: https://github.com/sonatype-nexus-community/jake
    rev: "v4.0.0"
    hooks:
      - id: scan

Whitelisting
~~~~~~~~~~~~

Vulnerabilities can be suppressed via a whitelist file. Pass the ``--whitelist`` argument with a path to a JSON file:

.. code-block::

    > jake guide --whitelist jake-whitelist.json

The file format is:

.. code-block:: json

    {"ignore": [{"id": "vulnerability-id-here", "reason": "reason"}]}

The ``id`` field is the vulnerability ID returned by Sonatype Guide. Any whitelisted ID will be excluded from the
results and will not cause a failure.

Check for vulnerabilities using Sonatype Lifecycle
--------------------------------------------------------

Access Sonatype's proprietary vulnerability data constrained by *your* Organizational Policy using ``jake``:

.. code-block::

    > jake iq --help

    usage: jake iq [-h] [-f FILE_PATH] [-t TYPE] -s https://localhost:8070 -i APP_ID -u USER_ID -p PASSWORD [-st STAGE]

    options:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is
                            not specified directly here, then we will attempt to
                            read data from STDIN. If there is no data on STDIN, we
                            will then fall back to looking for standard files in
                            the current directory that relate to the type of input
                            indicated by the -t flag.
      -t TYPE, -it TYPE, --type TYPE, --input-type TYPE
                            how jake should find the packages from which to
                            generate your SBOM. ENV = Read from the current Python
                            Environment; CONDA = Read output from `conda list
                            --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV =
                            read from Pipfile.lock; POETRY = read from a
                            poetry.lock. (Default = ENV)
      -s https://localhost:8070, --server-url https://localhost:8070
                            Full http(s):// URL to your Sonatype Lifecycle server
      -i APP_ID, --application-id APP_ID
                            Public Application ID in Sonatype Lifecycle
      -u USER_ID, --username USER_ID
                            Username for authentication to Sonatype Lifecycle
      -p PASSWORD, --password PASSWORD
                            Password for authentication to Sonatype Lifecycle
      -st STAGE, --stage STAGE
                            The stage for the report

So passing parameters that suit your Sonatype Lifecycle environment you can get a report:

.. code-block::

    > jake iq -s https://my-sonatype-lifecycle -i APP_ID -u USERNAME -p PASSWORD

Migrating from OSS Index to Sonatype Guide
------------------------------------------

jake v4.0.0 replaces the ``ddt`` (OSS Index) command with ``guide`` (Sonatype Guide). The two services use
compatible vulnerability data and the same PURL-based lookup mechanism, so migration is straightforward.

Command rename
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - v3 (OSS Index)
     - v4 (Sonatype Guide)
   * - ``jake ddt``
     - ``jake guide``
   * - ``jake ddt -t PIP -f requirements.txt``
     - ``jake guide -t PIP -f requirements.txt``

The ``ddt`` subcommand still exists in v4 as a deprecated alias and will be removed in a future release.

Environment variables
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - v3 variable
     - v4 variable
     - Notes
   * - ``OSS_INDEX_USERNAME``
     - ``SONATYPE_GUIDE_USERNAME``
     - ``OSS_INDEX_USERNAME`` still accepted as a fallback
   * - ``OSS_INDEX_TOKEN``
     - ``SONATYPE_GUIDE_TOKEN``
     - ``OSS_INDEX_TOKEN`` still accepted as a fallback

Account and API token
~~~~~~~~~~~~~~~~~~~~~

Sonatype Guide uses the same account system as OSS Index. If you already have an OSS Index account your
existing username and API token will work unchanged — only the environment variable names differ.

Breaking changes in v4
~~~~~~~~~~~~~~~~~~~~~~

- Python 3.7, 3.8, and 3.9 are no longer supported. Python 3.10+ is required.
- ``jake ddt`` is deprecated; use ``jake guide``.
- The ``--clear-cache`` flag has been removed (Sonatype Guide has no local cache).
- CycloneDX SBOM schema version default raised from 1.4 to 1.6.
- The ``ossindex-lib`` dependency has been replaced by ``sonatype-guide-api-client``.


.. _Sonatype Guide: https://guide.sonatype.com
.. _guide.sonatype.com: https://guide.sonatype.com
