<!--

    Copyright 2019-Present Sonatype Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

-->

![Jake Logo](https://github.com/sonatype-nexus-community/jake/blob/main/docs/images/jake.png)

# Jake

[![CircleCI](https://circleci.com/gh/sonatype-nexus-community/jake.svg?style=svg)](https://circleci.com/gh/sonatype-nexus-community/jake) 

`jake` is a tool to check for vulnerabilities in your Conda environments, powered by [Sonatype OSS Index](https://ossindex.sonatype.org/), that can also be used with [Sonatype's Nexus IQ Server](https://www.sonatype.com/product-nexus-lifecycle).

### Usage

```
$ jake --help
Usage: jake [OPTIONS] COMMAND [ARGS]...

  Jake: Put your python deps in a chokehold.

Options:
  -v, --version  Print version and exit
  --clear        Clear the OSS Index cache and exit
  --help         Show this message and exit.

Commands:
  config  Allows a user to set Nexus IQ or OSS Index config params...
  ddt     SPECIAL MOVE Allows you to perform scans backed by Sonatype's OSS...
  iq      EXTRA SPECIAL MOVE Allows you to perform scans backed by...
  sbom    Generates a purl only bom (no vulns) and outputs it to std_out by...

$ jake ddt --help
Usage: jake ddt [OPTIONS]

  SPECIAL MOVE

  Allows you to perform scans backed by Sonatype's OSS Index

  Example usage:

      Python scan: jake ddt

      Conda scan: conda list | jake ddt -c

Options:
  -vv, --verbose      Set log level to verbose
  -q, --quiet         Suppress cosmetic and informational output
  -c, --conda         Resolve conda dependencies from std_in
  -t, --targets TEXT  List of site packages containing modules to be evaluated
  --help              Show this message and exit.
```

`jake` can be run against either pypi or conda installed dependencies.

Conda: `conda list | jake ddt -c`

  Feeds your Conda dependencies from `conda list` by piping the output to `jake`

PyPi: `jake ddt`

  Feeds dependencies available to pip in the current scope (run `pip3 freeze` to see what those are)

### Options

You may also run `jake ddt` with `-vv` for a slew of debug data, in case you are running in to an odd situation, or you want to help out on development!

You can also run `jake ddt --clear` to clean out your local cache if desired. We cache results from OSS Index for 12 hours to prevent you from potentially getting rate limited (as your dependencies likely won't change super often).

You can also run `jake config ossi` to set optional configuration of your OSS Index username and API Key so that you can run more requests without getting rate limited. You may register for an account [at this link](https://ossindex.sonatype.org/user/register), and see [the information provided here](https://ossindex.sonatype.org/doc/rest) on Rate Limiting for why this is useful.

#### Usage with Nexus IQ Server

```
$ jake iq --help
Usage: jake iq [OPTIONS]

  EXTRA SPECIAL MOVE

  Allows you to perform scans backed by Sonatype's Nexus IQ Server

  Example usage:

      Python scan: jake iq -a <AppId>

      Conda scan: conda list | jake iq -a <AppId> -c

  Will pull values for other params from config unless overwritten here

      To set the IQ config: jake config iq

Options:
  -vv, --verbose                  Set log level to verbose
  -q, --quiet                     Suppress cosmetic and informational output
  -c, --conda                     Resolve conda dependencies from std_in
  -t, --targets TEXT              List of site packages containing modules to
                                  be evaluated

  -i, --insecure                  Allow jake to communicate with insecure
                                  endpoints

  -a, --application TEXT          Supply an IQ Server Public Application ID
                                  [required]

  -s, --stage [develop|build|stage-release|release]
                                  Specify a stage
  -u, --user TEXT                 Set username for Sonatype IQ
  -p, --password TEXT             Set password or token for associated user
  -h, --host TEXT                 Specify an endpoint for Sonatype IQ
  --help                          Show this message and exit.
```

`jake` can be used against Sonatype IQ if your company has an enterprise license.

Run `jake config iq` to set the the endpoint and auth params.

Once configured with proper credentials, run `jake iq -a <AppId>`, replacing `<AppId>` with the public ID of your application in Sonatype IQ. If a policy is violated that has the action set to `Fail` in IQ, `jake` will exit with a non-zero code which can be picked up by build automation or used to notify locally.

If your Nexus IQ installation is using a self-signed certificate, you can run `jake` with the `-i` or `--insecure` flag to work with these types of installations.

Each `jake` scan will generate a Software Bill of Materials (SBOM) in IQ and will output direct link to console.  The develop stage is used by default as opposed to other stages which usually correspond to component inventories of the latest build for a stage.

Some examples of using `jake` with Sonatype IQ

  1. (Onetime) Configure `jake` to use your Nexus IQ Server credentials:

        ```
        $ jake config iq
        Please enter your username for your IQ Server account: admin
        Please enter your user token for IQ Server: admin123
        Please provide the location of your IQ Server: http://localhost:8070
        ```

  2. (PyPi) Run `jake` against the AppId which will submit your dependencies to IQ and generate a report.

        ```
        (.venv) $ jake iq -a sandbox-application
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
        
        
        
        Jake version: v0.2.58
        Put your python deps in a chokehold.
        🐍  Collecting Dependencies from System...
        🐍  Parsing Coordinates...
        🐍  Generating CycloneDx BOM...
        🐍  Submitting to Sonatype IQ...
        🧨  Reticulating splines...
        Something slithers around your ankle! There are policy warnings from Sonatype IQ.
        Your IQ Server Report is available here: http://localhost:8070/ui/links/application/sandbox-application/report/d2ef2ebb08fd45daa520e149b8d413f3
        ```
  3. (Conda) Use `conda list` and the `-c` flag to pipe conda managed deps into `jake` to generate a report in Sonatype IQ
        ```
        $ conda list | jake iq -a conda-base -c
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

        Jake version: v0.1.4
        Put your python deps in a chokehold.
        🐍  Collecting Dependencies from System...
        🐍  Parsing Coordinates...
        🐍  Generating CycloneDx BOM...
        🐍  Submitting to Sonatype IQ...
        💥  Reticulating splines...
        Snakes on the plane! There are policy failures from Sonatype IQ.
        Your IQ Server Report is available here: http://localhost:8070/ui/links/application/conda-base/report/966f5ff7d2e44bb1bb14a6567e66b1ef
        ```

#### Usage with Virtual Environments

`jake` will resolve dependencies based off of what the current pip scope has access to.

If you do not have a virtual environment activated, `jake` will resolve the pip-managed pypi modules accessible to the system python shell:

```
  $ jake ddt -q
  🐍  Collecting Dependencies
  🐍  Querying OSS Index
  🐍  Auditing results from OSS Index
  ...
  [71/72] - pkg:pypi/pyjwt@1.3.0?extension=tar.gz [VULNERABLE] 1 known vulnerabilities forthis version
  ID: 4dc8bf86-e2ee-45b0-881f-bb4f03748b5b
  Title: [CVE-2017-11424]  Improper Access Control
  Description: In PyJWT 1.5.0 and below the `invalid_strings` check in `HMACAlgorithm.prepare_key` does not account for all PEM encoded public keys. Specifically, the PKCS1 PEM encoded format would be allowed because it is prefaced with the string `-----BEGIN RSA PUBLIC KEY-----` which is not accounted for. This enables symmetric/asymmetric key confusion attacks against users using the PKCS1 PEM encoded public keys, which would allow an attacker to craft JWTs from scratch.
  CVSS Score: 7.5 - High
  CVSS Vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
  CVE: CVE-2017-11424
  Reference: https://ossindex.sonatype.org/vuln/4dc8bf86-e2ee-45b0-881f-bb4f03748b5b
  ----------------------------------------------------
  [72/72] - pkg:pypi/python-apt@1.1.0b1%20ubuntu0.16.4.8?extension=tar.gz - no known vulnerabilities for this version
```

You can install `jake` in a virtual environment and it will be scoped to the dependencies that python shell has access to, but you would end up getting a report that includes jake's own dependencies.  To get around this, we added the `-t, --targets` flag which allows you to pass in a list site/dist package directories containing modules outside of the scope that `jake` is executing in.

To get the site packages available to a virtual environment:

```
  $ source .venv/bin/activate
  (.venv) $ python -m site
  sys.path = [
      '/home/ButterB0wl/git_repos/jake',
      '/usr/lib/python37.zip',
      '/usr/lib/python3.7',
      '/usr/lib/python3.7/lib-dynload',
      '/home/ButterB0wl/git_repos/jake/.venv/lib/python3.7/site-packages',
  ]
  USER_BASE: '/home/ButterB0wl/.local' (exists)
  USER_SITE: '/home/ButterB0wl/.local/lib/python3.7/site-packages' (exists)
  ENABLE_USER_SITE: False
```

The `-t` argument accepts a list as a string literal.  This is the best way I've found to do this, if you find a better way please create an issue :)

Run the python command using the shell you want to target and export to an env var:

```
  # using target python shell for system or virtual environment
  $ export JAKE_TARGET=`python -c "import site; print(site.getsitepackages())"`
  # using whatever shell has access to the jake module, can be a global install or stand-alone virtual environment
  $ jake ddt -t "$JAKE_TARGET"
```

In other words: activate the virtual environment, run the `site.getsitepackages()` command, and make the output accessible to your `jake` install

This will work for the `ddt`, `iq`, and `sbom` subcommands when evaluating pip modules.

To target a conda environment, specify it using `conda list` piped into `jake` with the `-c` flag.

## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

Who better to wrangle those slippery deps in any virtual or real environment.

## Installation

### Download from PyPI

`pip3 install jake`

### Build from source

* Clone the repo
* Install Python 3.7 or higher
* Ensure pip3 is installed (it should be)
* Run `python3 -m venv .venv` (or whatever virtual environment you prefer)
* Run `source .venv/bin/activate`
* Run `pip3 install -r requirements.txt`
* Run `pip3 install -e .`

Once you've done this, you should have `jake` available to test with fairly globally, pointed at the local source you've cloned.

## Development

`jake` is written using Python 3.7

This project also uses `pip3` for dependencies, so you will need to download make sure you have `pip3`.

Follow instructions in [Build from source](#build-from-source).

Tests can be run with `python3 -m unittest discover`

More TBD.

## Misc

We have a nightly "internal" build that scans Jake using Nexus Lifecycle. Files related to this build are:

   * [Jenkinsfile](./Jenkinsfile)
   * [license-excludes.xml](./license-excludes.xml) - define which files to skip during header checks.

You should be able to ignore these file for the most part.    
    
## Contributing

We care a lot about making the world a safer place, and that's why we created `jake`. If you as well want to
speed up the pace of software development by working on this project, jump on in! Before you start work, create
a new issue, or comment on an existing issue, to let others know you are!

## Releasing

We use [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) to generate patch releases
from commits to the `main` branch.

For example, to perform a "patch" release, add a commit to `main` with a comment like:

```
fix: Resolve vulnerability: CVE-2020-27783 in lxml
```

To avoid performing a release after a commit to the `main` branch, be sure your commit message includes `[skip ci] `.

## The Fine Print

Remember:

* If you are a Sonatype customer, you may file Sonatype support tickets related to `jake` support in regard to this project
  * We suggest you file issues here on GitHub as well, so that the community can pitch in
* If you are not a Sonatype customer, Do NOT file Sonatype support tickets related to `jake` support in regard to this project, file an issue here on GitHub

Have fun creating and using `jake` and the [Sonatype OSS Index](https://ossindex.sonatype.org/), we are glad to have you here!

## Getting help

Looking to contribute to our code but need some help? There's a few ways to get information:

* Chat with us on [Gitter](https://gitter.im/sonatype/nexus-developers)
