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

<p align="center">
    <img src="https://raw.githubusercontent.com/sonatype-nexus-community/jake/main/docs/images/jake.png" width="350" alt="jake icon"/>
</p>

# Jake

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/sonatype-nexus-community/jake/Python%20CI)
![Python Version Support](https://img.shields.io/badge/python-3.6+-blue)
![PyPI Version](https://img.shields.io/pypi/v/jake?label=PyPI&logo=pypi)
[![GitHub license](https://img.shields.io/github/license/sonatype-nexus-community/jake)](https://github.com/sonatype-nexus-community/jake/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/sonatype-nexus-community/jake)](https://github.com/sonatype-nexus-community/jake/issues)
[![GitHub forks](https://img.shields.io/github/forks/sonatype-nexus-community/jake)](https://github.com/sonatype-nexus-community/jake/network)
[![GitHub stars](https://img.shields.io/github/stars/sonatype-nexus-community/jake)](https://github.com/sonatype-nexus-community/jake/stargazers)

----

`jake` is a tool to check for your Python environments and applications that can:
- produce CycloneDX software bill-of-materials
- report on known vulnerabilities

`jake` is powered by [Sonatype OSS Index](https://ossindex.sonatype.org) and can also be used with 
[Sonatype's Nexus IQ Server](https://www.sonatype.com/product-nexus-lifecycle).

## Installation

Install from pypi.org as you would any other Python module:

```
pip install jake
```

or 

```
poetry add jake
```

_Other Python package managers are available._

## Usage

### Getting Started

`jake` can guide you...

```
> jake --help
usage: jake [-h] [-v] [-X]  ...

Put your Python dependencies in a chokehold

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show which version of jake you are running
  -w, --warn-only   prevents exit with non-zero code when issues have been
                    detected
  -X                enable debug output

Jake sub-commands:

    iq              perform a scan backed by Nexus Lifecycle
    ddt             perform a scan backed by OSS Index
    sbom            generate a CycloneDX software-bill-of-materials (no vulnerabilities)
```

`jake` will exit with code `0` under normal operation and `1` if vulnerabilities are found (OssIndex) or Policy 
Violations are detected (Nexus IQ), unless you pass the `-w` flag in which case `jake` will always exit with code `0`....

### Check for vulnerabilities using OSS Index

`jake` will look at the packaged installed in your current Python environment and check these against OSS Index for you.
Optionally, it can create a CycloneDX software bill-of-materials at the same time in a format that suits you.

```
> jake ddt --help

usage: jake ddt [-h] [--clear-cache] [-o PATH/TO/FILE] [--output-format {xml,json}] [--schema-version {1.2,1.1,1.0,1.3}]

optional arguments:
  -h, --help            show this help message and exit
  --clear-cache         Clears any local cached OSS Index data prior to execution
  -o PATH/TO/FILE, --output-file PATH/TO/FILE
                        Specify a file to output the SBOM to. If not specified the report will be output to the console. STDOUT is not supported.
  --output-format {xml,json}
                        SBOM output format (default = xml)
  --schema-version {1.2,1.1,1.0,1.3}
                        CycloneDX schema version to use (default = 1.3)
```

So you can quickly get a report by running:

```
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
                                                  
                                                  

Jake Version: 1.0.0
Put your Python dependencies in a chokehold.

🐍 Collected 42 packages from your environment (0:00:00.10)
🐍 Successfully queried OSS Index for package and vulnerability info (0:00:00.59)
🐍 Sane number of results from OSS Index


╔Summary═══════════════╦════╗
║ Audited Dependencies ║ 42 ║
╠══════════════════════╬════╣
║ Vulnerablities Found ║ 0  ║
╚══════════════════════╩════╝
```

### Check for vulnerabilities using Sonatype Nexus Lifecycle

Access Sonatype's proprietary vulnerability data using `jake`:

```
> jake iq --help

usage: jake iq [-h] -s https://localhost:8070 -i APP_ID -u USER_ID -p PASSWORD

optional arguments:
  -h, --help            show this help message and exit
  -s https://localhost:8070, --server-url https://localhost:8070
                        Full http(s):// URL to your Nexus Lifecycle server
  -i APP_ID, --application-id APP_ID
                        Public Application ID in Nexus Lifecycle
  -u USER_ID, --username USER_ID
                        Username for authentication to Nexus Lifecycle
  -p PASSWORD, --password PASSWORD
                        Password for authentication to Nexus Lifecycle
```

So passing parameters that suit your Nexus Lifecycle environment you can get a report:

```
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
                                                  
                                                  

Jake Version: 1.0.0
Put your Python dependencies in a chokehold

🐍 IQ Server at https://my-nexus-lifecyle is up and accessible (0:00:00.14)
🐍 Collected 42 packages from your environment (0:00:00.09)
🧨 Something slithers around your ankle! There are policy warnings from Sonatype Nexus IQ. (0:00:11.50)

Your Sonatype Nexus IQ Lifecycle Report is available here:
  HTML: https://my-nexus-lifecyle/ui/links/application/APP_ID/report/4831bcb7fbaa45c3a2481048e446b598
  PDF:  https://my-nexus-lifecyle/ui/links/application/APP_ID/report/4831bcb7fbaa45c3a2481048e446b598/pdf
```

## Why Jake?

Jake The Snake was scared of Snakes. The finishing move was DDT. He finishes the Snake with DDT.

Who better to wrangle those slippery dependencies in any virtual or real environment.

## Python Support

We endeavour to support all functionality for all [current actively supported Python versions](https://www.python.org/downloads/).
However, some features may not be possible/present in older Python versions due to their lack of support.

## Changelog

See our [CHANGELOG](./CHANGELOG.md).

## The Fine Print

Remember:

It is worth noting that this is **NOT SUPPORTED** by Sonatype, and is a contribution of ours to the open source
community (read: you!)

* Use this contribution at the risk tolerance that you have
* Do NOT file Sonatype support tickets related to `ossindex-lib`
* DO file issues here on GitHub, so that the community can pitch in

Phew, that was easier than I thought. Last but not least of all - have fun!