<p align="center">
    <img src="https://github.com/sonatype-nexus-community/jake/blob/master/docs/images/SON_Jake_the_Snake_Logo_v3@2x.png" width="350"/>
</p>

# Jake

[![CircleCI](https://circleci.com/gh/sonatype-nexus-community/jake.svg?style=svg)](https://circleci.com/gh/sonatype-nexus-community/jake) 

`jake` is a tool to check for vulnerabilities in your Conda environments, powered by [Sonatype OSS Index](https://ossindex.sonatype.org/), that can also be used with [Sonatype's Nexus IQ Server](https://www.sonatype.com/product-nexus-lifecycle).

### Usage

```
$ Usage: jake [OPTIONS] COMMAND [ARGS]...

  Jake: Put your python deps in a chokehold.

Options:
  -v, --version  Print version and exit
  --help         Show this message and exit.

Commands:
  config  Allows a user to set Nexus IQ or OSS Index config params...
  ddt     SPECIAL MOVE Allows you to perform scans backed by Sonatype's OSS...
  iq      EXTRA SPECIAL MOVE Allows you to perform scans backed by...


$ Usage: jake ddt [OPTIONS]

  SPECIAL MOVE

  Allows you to perform scans backed by Sonatype's OSS Index

  Example usage:

      Python scan: jake ddt

      Conda scan: conda list | jake ddt -c

      Clear cache: jake ddt --clear

Options:
  -vv, --verbose  Set log level to verbose
  -q, --quiet     Suppress cosmetic and informational output
  --clear         Clear the OSS Index cache
  -c, --conda     Resolve conda dependencies from std_in
  --help          Show this message and exit.
```

`jake` can be run against either pypi or conda installed dependencies.

Conda: `conda list | jake ddt -c`

  Feeds your Conda dependencies from `conda list` by piping the output to `jake`

PyPi: `jake ddt`

  Feeds dependencies available to pip in the current scope (run `pip freeze` to see what those are)

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
  -a, --application TEXT          Supply an IQ Server Public Application ID
                                  [required]

  -s, --stage [develop|build|stage-release|release]
                                  Specify a stage
  -u, --user TEXT                 Set username for Sonatype IQ
  -p, --password TEXT             Set password or token for associated user
  -h, --host TEXT                 Specify an endpoint for Sonatype IQ
  -c, --conda                     Resolve conda dependencies from std_in
  --help                          Show this message and exit.
```

`jake` can be used against Sonatype IQ if your company has an enterprise license.

Run `jake config iq` to set the the endpoint and auth params.

Once configured with proper credentials, run `jake iq -a <AppId>`, replacing `<AppId>` with the public ID of your application in Sonatype IQ. If a policy is violated that has the action set to `Fail` in IQ, `jake` will exit with a non zero code which can be picked up build automation or used to notify locally.

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
        (.venv) ajurgenson@ArtieSonaDell:~/git_repos/jake$ jake iq -a jake
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



        Jake version: v0.0.21
        Put your python deps in a chokehold.
        ✅  Calling OSS Index
        ✅  Calling Nexus IQ Server
        Your IQ Server Report is available here: http://localhost:8070/ui/links/application/jake/report/2099ab2ce0dc4ea7a034ee227ba431f9
        All good to go! Smooth sailing for you! No policy violations reported by IQ Server
        ```
  3. (Conda) Use `conda list` and the `-c` flag to pipe conda managed deps into `jake` to generate a report in Sonatype IQ
        ```
        $ conda list | jake iq -c -a jake
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

        Jake version: v0.0.21
        Put your python deps in a chokehold.
        ✅  Calling OSS Index
        💥  Calling Nexus IQ Server
        Your IQ Server Report is available here: http://localhost:8070/ui/links/application/jake/report/6adf87e96f72441c8606d2c2a2eca874
        Your build has failed, please check your IQ Server Report for more information
        ```

#### Usage with Virtual Environments

`jake` will resolve dependencies based off of what the current pip scope has access to.

If you do not have a virtual environment activated, `jake` will resolve the pip-managed pypi packages installed to the system:

```
  $ jake ddt -q
  ✅  Collecting Dependencies
  ✅  Querying OSS Index
  ✅  Auditing results from OSS Index
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


## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

Who better to wrangle those slippery deps in any virtual or real environment.

## Installation

### Download from PyPI

`pip3 install jake`

### Build from source

* Clone the repo
* Install Python 3.7 or higher
* Ensure pip is installed (it should be)
* Run `python3 -m venv .venv` (or whatever virtual environment you prefer)
* Run `source .venv/bin/activate`
* Run `pip install -r requirements.txt`
* Run `pip install -e .`

Once you've done this, you should have `jake` available to test with fairly globally, pointed at the local source you've cloned.

## Development

`jake` is written using Python 3.7

This project also uses `pip` for dependencies, so you will need to download make sure you have `pip`.

Follow instructions in [Build from source](#build-from-source).

Tests can be run with `python3 -m unittest discover`

More TBD.

## Contributing

We care a lot about making the world a safer place, and that's why we created `jake`. If you as well want to
speed up the pace of software development by working on this project, jump on in! Before you start work, create
a new issue, or comment on an existing issue, to let others know you are!

## The Fine Print

It is worth noting that this is **NOT SUPPORTED** by Sonatype, and is a contribution of ours
to the open source community (read: you!)

Remember:

* Use this contribution at the risk tolerance that you have
* Do NOT file Sonatype support tickets related to `jake` support in regard to this project
* DO file issues here on GitHub, so that the community can pitch in

Phew, that was easier than I thought. Last but not least of all:

Have fun creating and using `jake` and the [Sonatype OSS Index](https://ossindex.sonatype.org/), we are glad to have you here!

## Getting help

Looking to contribute to our code but need some help? There's a few ways to get information:

* Chat with us on [Gitter](https://gitter.im/sonatype/nexus-developers)
