<p align="center">
    <img src="https://github.com/sonatype-nexus-community/snek/blob/master/docs/images/nothing.png" width="350"/>
</p>

# Jake

[![CircleCI](https://circleci.com/gh/sonatype-nexus-community/jake.svg?style=svg)](https://circleci.com/gh/sonatype-nexus-community/jake) 

`jake` is a tool to check for vulnerabilities in your Conda environments, powered by [Sonatype OSS Index](https://ossindex.sonatype.org/).

### Usage

```
$ jake --help
usage: jake [-h] [-V] [-VV] [-C] {ddt}

positional arguments:
  {ddt}           run jake

optional arguments:
  -h, --help      show this help message and exit
  -V, --version   show program version
  -VV, --verbose  set verbosity level to debug
  -C, --clean     wipe out jake cache
```

Typical usage of `jake` is to run it like so: `conda list | jake ddt`, which will feed your Conda dependencies in your current Conda environment to `jake`, which will then reach out and check OSS Index to see if they are vulnerable!

### Options

You may also run `jake` with `-VV` for a slew of debug data, in case you are running in to an odd situation, or you want to help out on development!

You can also run `jake -C` to clean out your local cache if desired. We cache results from OSS Index for 12 hours to prevent you from potentially getting rate limited (as your dependencies likely won't change super often). 

## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

## Installation

### Download from PyPI

TBD

### Build from source

* Clone the repo
* Install Python 3.7 or higher
* Ensure pip is installed (it should be)
* Run `python3 venv .venv` (or whatever virtual environment you prefer)
* Run `source .venv/bin/activate`
* Run `pip install -r requirements`
* Run `pip install -e .`

Once you've done this, you should have `jake` available to test with fairly globally, pointed at the local source you've cloned.

## Development

`jake` is written using Python 3.7

This project also uses `pip` for dependencies, so you will need to download make sure you have `pip`.

Follow instructions in Build from source.

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
