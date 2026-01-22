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

`jake` can guide you...

.. code-block::

    > jake --help
    usage: jake [-h] [-v] [-w] [-X]  ...

    Put your Python dependencies in a chokehold

    optional arguments:
      -h, --help       show this help message and exit
      -v, --version    show which version of jake you are running
      -w, --warn-only  prevents exit with non-zero code when issues have been
                       detected
      -X               enable debug output

    Jake sub-commands:

        iq             perform a scan backed by Nexus Lifecycle
        ddt            perform a scan backed by OSS Index
        sbom           generate a CycloneDX software-bill-of-materials (no
                       vulnerabilities)


``jake`` will exit with code ``0`` under normal operation and ``1`` if vulnerabilities are found (Oss Index) or Policy
Violations are detected (Nexus IQ), unless you pass the ``-w`` flag in which case ``jake`` will always exit with code
``0``.

Generating an SBOM
------------------

``jake`` can take data from various inputs (or just look at your current Python environment) and produce a CycloneDX for
you.

.. code-block::

    > jake sbom --help

    usage: jake sbom [-h] [-f FILE_PATH] [-t TYPE] [-o PATH/TO/FILE]
                       [--output-format {json,xml}]
                       [--schema-version {1.0,1.1,1.2,1.3}]

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is
                            not specified directly here,then we will attempt to
                            read data from STDIN. If there is no data on STDIN, we
                            will then fall back to looking for standard files in
                            the current directory that relate to the type of input
                            indicated by the -t flag.
      -t TYPE, --type TYPE, -it TYPE, --input-type TYPE
                            how jake should find the packages from which to
                            generate your SBOM.ENV = Read from the current Python
                            Environment; CONDA = Read output from `conda list
                            --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV =
                            read from Pipfile.lock; POETRY = read from a
                            poetry.lock. (Default = ENV)
      -o PATH/TO/FILE, --output-file PATH/TO/FILE
                            Specify a file to output the SBOM to
      --output-format {json,xml}
                            SBOM output format (default = xml)
      --schema-version {1.0,1.1,1.2,1.3}
                            CycloneDX schema version to use (default = 1.3)

Check out these examples using STDIN:

.. code-block::

    conda list --explicit --md5 | jake sbom -t CONDA
    conda list --json | jake sbom -t CONDA_JSON
    cat /path/to/Pipfile.lock | jake sbom -t PIPENV


Check out these examples specifying a manifest:

.. code-block::

    jake sbom -t PIP -f /path/to/requirements.txt
    jake sbom -t PIPENV -f /path/to/Pipfile.lock


Check for vulnerabilities using OSS Index
-----------------------------------------

``jake`` will look at the packaged installed in your current Python environment and check these against OSS Index for
you.

.. code-block::

    > jake ddt --help

    usage: jake ddt [-h] [-f FILE_PATH] [-t TYPE] [--clear-cache] [--oss-host URL] [-o PATH/TO/FILE] [--output-format {json,xml}] [--schema-version {1.2,1.3,1.4,1.1,1.0}] [--whitelist OSS_WHITELIST_JSON_FILE]

    options:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is not specified directly here,then we will attempt to read data from STDIN. If there is no data on STDIN, we will then fall back to looking for standard
                            files in the current directory that relate to the type of input indicated by the -t flag.
      -t TYPE, -it TYPE, --type TYPE, --input-type TYPE
                            how jake should find the packages from which to generate your SBOM.ENV = Read from the current Python Environment; CONDA = Read output from `conda list --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV = read from Pipfile.lock; POETRY = read from a poetry.lock. (Default = ENV)
      --clear-cache         Clears any local cached OSS Index data prior to execution
      --oss-host URL        Specify a custom OSS Index host URL (default = https://ossindex.sonatype.org)
      -o PATH/TO/FILE, --output-file PATH/TO/FILE
                            Specify a file to output the SBOM to. If not specified the report will be output to the console. STDOUT is not supported.
      --output-format {json,xml}
                            SBOM output format (default = xml)
      --schema-version {1.2,1.3,1.4,1.1,1.0}
                            CycloneDX schema version to use (default = 1.4)
      --whitelist OSS_WHITELIST_JSON_FILE
                            Set path to whitelist json file

So you can quickly get a report by running:

.. code-block::

    > jake ddt

                       ___           ___           ___
           ___        /  /\         /  /\         /  /\
          /__/\      /  /::\       /  /:/        /  /::\
          \__\:\    /  /:/\:\     /  /:/        /  /:/\:\
      ___ /  /::\  /  /::\ \:\   /  /::\____   /  /::\ \:\
     /__/\  /:/\/ /__/:/\:\_\:\ /__/:/\:::::\ /__/:/\:\ \:\
     \  \:\/:/~~  \__\/  \:\/:/ \__\/~|:|~~~~ \  \:\ \:\_\/
      \  \::/          \__\::/     |  |:|      \  \:\ \:\
       \__\/           /  /:/      |  |:|       \  \:\_\/
                      /__/:/       |__|:|        \  \:\
                      \__\/         \__\|         \__\/


                /)                     /)
            _/_(/    _     _  __   _  (/_   _
     o   o  (__/ )__(/_   /_)_/ (_(_(_/(___(/_ o   o



    Jake Version: 2.1.1
    Put your Python dependencies in a chokehold.

    🐍 Collected 42 packages from your environment (0:00:00.10)
    🐍 Successfully queried OSS Index for package and vulnerability info (0:00:00.59)
    🐍 Sane number of results from OSS Index


    ╔Summary═══════════════╦════╗
    ║ Audited Dependencies ║ 42 ║
    ╠══════════════════════╬════╣
    ║ Vulnerablities Found ║ 0  ║
    ╚══════════════════════╩════╝

This is what ``jake`` will output if any bad things are found:

.. code-block::

                       ___           ___           ___
           ___        /  /\         /  /\         /  /\
          /__/\      /  /::\       /  /:/        /  /::\
          \__\:\    /  /:/\:\     /  /:/        /  /:/\:\
      ___ /  /::\  /  /::\ \:\   /  /::\____   /  /::\ \:\
     /__/\  /:/\/ /__/:/\:\_\:\ /__/:/\:::::\ /__/:/\:\ \:\
     \  \:\/:/~~  \__\/  \:\/:/ \__\/~|:|~~~~ \  \:\ \:\_\/
      \  \::/          \__\::/     |  |:|      \  \:\ \:\
       \__\/           /  /:/      |  |:|       \  \:\_\/
                      /__/:/       |__|:|        \  \:\
                      \__\/         \__\|         \__\/


                /)                     /)
            _/_(/    _     _  __   _  (/_   _
     o   o  (__/ )__(/_   /_)_/ (_(_(_/(___(/_ o   o



    Jake Version: 2.1.1
    Put your Python dependencies in a chokehold

    🐍 Collected 69 packages from your python environment                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% -:--:--
    🐍 Successfully queried OSS Index for package and vulnerability info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% -:--:--
    🐍 Sane number of results from OSS Index                             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% -:--:--
    🐍 Munching & crunching data...                                      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% -:--:--

    [59/69] - pkg:pypi/cryptography@2.2 [VULNERABLE]
    Vulnerability Details for pkg:pypi/cryptography@2.2
    ├── ⚠  ID: 333aca51-7375-4a9d-be64-16d316ab9274
    │   └── ╭─ CVE-2020-36242 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
    │       │                                                                                                                                                                                                                                                                                                              │
    │       │ In the cryptography package before 3.3.2 for Python, certain sequences of update calls to symmetrically encrypt multi-GB values could result in an integer overflow and buffer overflow, as demonstrated by the Fernet class.                                                                                │
    │       │                                                                                                                                                                                                                                                                                                              │
    │       │ Details:                                                                                                                                                                                                                                                                                                     │
    │       │   - CVSS Score: 9.1 - Critical                                                                                                                                                                                                                                                                               │
    │       │   - CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H                                                                                                                                                                                                                                                │
    │       │   - CWE: Unknown                                                                                                                                                                                                                                                                                             │
    │       │                                                                                                                                                                                                                                                                                                              │
    │       │ References:                                                                                                                                                                                                                                                                                                  │
    │       │   - https://ossindex.sonatype.org/vulnerability/333aca51-7375-4a9d-be64-16d316ab9274?component-type=pypi&component-name=cryptography&utm_source=python-oss-index-lib%400.2.1&utm_medium=integration                                                                                                          │
    │       │   - https://nvd.nist.gov/vuln/detail/CVE-2020-36242                                                                                                                                                                                                                                                          │
    │       │                                                                                                                                                                                                                                                                                                              │
    │       ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
    └── ⚠  ID: f19ff95c-cec5-4263-8d3b-e3e64698881e
        └── ╭─ CVE-2018-10903 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
            │                                                                                                                                                                                                                                                                                                              │
            │ A flaw was found in python-cryptography versions between >=1.9.0 and <2.3. The finalize_with_tag API did not enforce a minimum tag length. If a user did not validate the input length prior to passing it to finalize_with_tag an attacker could craft an invalid payload with a shortened tag (e.g. 1      │
            │ byte) such that they would have a 1 in 256 chance of passing the MAC check. GCM tag forgeries can cause key leakage.                                                                                                                                                                                         │
            │                                                                                                                                                                                                                                                                                                              │
            │ Details:                                                                                                                                                                                                                                                                                                     │
            │   - CVSS Score: 7.5 - High                                                                                                                                                                                                                                                                                   │
            │   - CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N                                                                                                                                                                                                                                                │
            │   - CWE: Unknown                                                                                                                                                                                                                                                                                             │
            │                                                                                                                                                                                                                                                                                                              │
            │ References:                                                                                                                                                                                                                                                                                                  │
            │   - https://ossindex.sonatype.org/vulnerability/f19ff95c-cec5-4263-8d3b-e3e64698881e?component-type=pypi&component-name=cryptography&utm_source=python-oss-index-lib%400.2.1&utm_medium=integration                                                                                                          │
            │   - https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2018-10903                                                                                                                                                                                                                                               │
            │   - https://github.com/pyca/cryptography/pull/4342/commits/688e0f673bfbf43fa898994326c6877f00ab19ef                                                                                                                                                                                                          │
            │   - https://nvd.nist.gov/vuln/detail/CVE-2018-10903                                                                                                                                                                                                                                                          │
            │                                                                                                                                                                                                                                                                                                              │
            ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

                        Summary
    ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Audited Dependencies ┃ Vulnerabilities Found ┃
    ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
    │ 69                   │ 2                     │
    └──────────────────────┴───────────────────────┘


Check out these examples using STDIN:

.. code-block::

    conda list --explicit --md5 | jake ddt -t CONDA
    conda list --json | jake ddt -t CONDA_JSON
    cat /path/to/Pipfile.lock | jake ddt -t PIPENV


Check out these examples specifying a manifest:

.. code-block::

    jake ddt -t PIP -f /path/to/requirements.txt
    jake ddt -t PIPENV -f /path/to/Pipfile.lock


Pre-commit Hook
~~~~~~~~~~~~~~~

A pre-commit hook is also available for use:

.. code-block:: yaml

  - repo: https://github.com/sonatype-nexus-community/jake
    rev: "v1.3.0"
    hooks:
      - id: scan

Check for vulnerabilities using Sonatype Nexus Lifecycle
--------------------------------------------------------

Access Sonatype's proprietary vulnerability data using ``jake``:

.. code-block::

    > jake iq --help

    usage: jake iq [-h] [-f FILE_PATH] [-t TYPE] -s https://localhost:8070 -i APP_ID -u USER_ID -p PASSWORD [-st STAGE]

    options:
      -h, --help            show this help message and exit
      -f FILE_PATH, --input-file FILE_PATH
                            Where to get input data from. If a path to a file is not specified directly here,then we will attempt to read data from STDIN. If there is no data on STDIN, we will then fall back to looking for standard
                            files in the current directory that relate to the type of input indicated by the -t flag.
      -t TYPE, -it TYPE, --type TYPE, --input-type TYPE
                            how jake should find the packages from which to generate your SBOM.ENV = Read from the current Python Environment; CONDA = Read output from `conda list --explicit`; CONDA_JSON = Read output from `conda list
                            --json`; PIP = read from a requirements.txt; PIPENV = read from Pipfile.lock; POETRY = read from a poetry.lock. (Default = ENV)
      -s https://localhost:8070, --server-url https://localhost:8070
                            Full http(s):// URL to your Nexus Lifecycle server
      -i APP_ID, --application-id APP_ID
                            Public Application ID in Nexus Lifecycle
      -u USER_ID, --username USER_ID
                            Username for authentication to Nexus Lifecycle
      -p PASSWORD, --password PASSWORD
                            Password for authentication to Nexus Lifecycle
      -st STAGE, --stage STAGE
                            The stage for the report

So passing parameters that suit your Nexus Lifecycle environment you can get a report:

.. code-block::

    > jake iq -s https://my-nexus-lifecyle -i APP_ID -u USERNAME -p PASSWORD

                       ___           ___           ___
           ___        /  /\         /  /\         /  /\
          /__/\      /  /::\       /  /:/        /  /::\
          \__\:\    /  /:/\:\     /  /:/        /  /:/\:\
      ___ /  /::\  /  /::\ \:\   /  /::\____   /  /::\ \:\
     /__/\  /:/\/ /__/:/\:\_\:\ /__/:/\:::::\ /__/:/\:\ \:\
     \  \:\/:/~~  \__\/  \:\/:/ \__\/~|:|~~~~ \  \:\ \:\_\/
      \  \::/          \__\::/     |  |:|      \  \:\ \:\
       \__\/           /  /:/      |  |:|       \  \:\_\/
                      /__/:/       |__|:|        \  \:\
                      \__\/         \__\|         \__\/


                /)                     /)
            _/_(/    _     _  __   _  (/_   _
     o   o  (__/ )__(/_   /_)_/ (_(_(_/(___(/_ o   o



    Jake Version: 2.1.1
    Put your Python dependencies in a chokehold

    🐍 IQ Server at https://my-nexus-lifecyle is up and accessible (0:00:00.14)
    🐍 Collected 42 packages from your environment (0:00:00.09)
    🧨 Something slithers around your ankle! There are policy warnings from Sonatype Nexus IQ. (0:00:11.50)

    Your Sonatype Nexus IQ Lifecycle Report is available here:
      HTML: https://my-nexus-lifecyle/ui/links/application/APP_ID/report/4831bcb7fbaa45c3a2481048e446b598
      PDF:  https://my-nexus-lifecyle/ui/links/application/APP_ID/report/4831bcb7fbaa45c3a2481048e446b598/pdf
