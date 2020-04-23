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

Typical usage of `jake` is to run it like so: `conda list | jake ddt`, which will feed your Conda dependencies in your current Conda environment to `jake`, which will then reach out and check OSS Index to see if they are vulnerable!

### Options

You may also run `jake ddt` with `-VV` for a slew of debug data, in case you are running in to an odd situation, or you want to help out on development!

You can also run `jake ddt -C` to clean out your local cache if desired. We cache results from OSS Index for 12 hours to prevent you from potentially getting rate limited (as your dependencies likely won't change super often). 

You can also run `jake ddt -S` to set optional configuration of your OSS Index username and API Key so that you can run more requests without getting rate limited. You may register for an account [at this link](https://ossindex.sonatype.org/user/register), and see [the information provided here](https://ossindex.sonatype.org/doc/rest) on Rate Limiting for why this is useful.

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

`jake` can be used against Nexus IQ Server, to audit your application using your organizations policy.

You can run `jake ddt -P` to set configuration of your IQ Server username and token.

Once you've configured `jake` with proper credentials, you can run `jake ddt -A application-id`, replacing `application-id` with the public ID of your application in IQ Server. If there is a policy action required after submitting to IQ Server, `jake` will exit with a non zero code, allowing you to fail builds based on needed policy actions. The IQ Server Report URL will be provided as well.

An example of using `jake` with the Nexus IQ Server `Sandbox Application` follows.

  1. (Onetime) Configure `jake` to use your Nexus IQ Server credentials:
  
        ```
        $ jake ddt -P
        Please enter your username for your IQ Server account: admin
        Please enter your user token for IQ Server: admin123
        Please provide the location of your IQ Server: http://localhost:8070
        ```
    
  1. Feed your Conda dependencies in your current Conda environment to `jake`, which will then reach out and check Nexus IQ Server to see if they are vulnerable:

        ```
        $ conda list | jake ddt -A sandbox-application
        ...
        Your IQ Server Report is available here: http://localhost:8070/ui/links/application/sandbox-application/report/fec66f75726f434cb8e94360a6c11df1
        All good to go! Smooth sailing for you! No policy violations reported by IQ Server
        ```

## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

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
