<p align="center">
    <img src="https://github.com/sonatype-nexus-community/jake/blob/master/docs/images/SON_Jake_the_Snake_Logo_v3@2x.png" width="350"/>
</p>

# Jake

[![CircleCI](https://circleci.com/gh/sonatype-nexus-community/jake.svg?style=svg)](https://circleci.com/gh/sonatype-nexus-community/jake) 

`jake` is a tool to check for vulnerabilities in your Conda environments, powered by [Sonatype OSS Index](https://ossindex.sonatype.org/).

### Usage

```
$ jake --help
usage: jake {ddt} [-h] [-V] [-VV] [-C] [-S]

positional arguments:
  {ddt}           run jake

optional arguments:
  -h, --help      show this help message and exit
  -V, --version   show program version and exit
  -VV, --verbose  set verbosity level to debug
  -C, --clean     wipe out jake cache
  -S, --snake     set optional jake config
```

Typical usage of `jake` is to run it like so: `conda list | jake ddt`, which will feed your Conda dependencies in your current Conda environment to `jake`, which will then reach out and check OSS Index to see if they are vulnerable!

### Options

You may also run `jake ddt` with `-VV` for a slew of debug data, in case you are running in to an odd situation, or you want to help out on development!

You can also run `jake ddt -C` to clean out your local cache if desired. We cache results from OSS Index for 12 hours to prevent you from potentially getting rate limited (as your dependencies likely won't change super often). 

You can also run `jake ddt snake` to set optional configuration of your OSS Index username and API Key so that you can run more requests without getting rate limited. You may register for an account [at this link](https://ossindex.sonatype.org/user/register), and see [the information provided here](https://ossindex.sonatype.org/doc/rest) on Rate Limiting for why this is useful.

## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

## Installation

### Download from PyPI

`pip3 install jake`

### Build from source

* Clone the repo
* Install Python 3.7 or higher
* Ensure pip is installed (it should be)
* Run `python3 venv .venv` (or whatever virtual environment you prefer)
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
