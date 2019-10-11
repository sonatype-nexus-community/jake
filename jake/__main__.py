# Copyright 2019 Sonatype Inc.
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
import sys
import argparse
import logging
import json

from conda.cli.python_api import Commands, run_command
from os import _exit, EX_OSERR

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse
from jake.audit.audit import Audit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('run', help='run jake', choices=['ddt'])
    parser.add_argument('-V', '--version', help='show program version', action='store_true')
    parser.add_argument('-E', '--env', help="conda environment to run", default='root')
    parser.add_argument('-VV', '--verbose', help="set verbosity level to debug", action='store_true')
    args = parser.parse_args()
    log = logging.getLogger('jake')
    if args.verbose:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.ERROR)

    parse = Parse()
    ossindex = OssIndex()
    audit = Audit()
    
    if args.run == 'ddt':
        log.info('Calling OSS Index')
        env = args.env
        purls = parse.getDependencies(run_command_list=run_command(Commands.LIST, "-n " + env))
        if purls is None:
            log.error("No purls returned, likely culprit is no Conda installed")
            _exit(EX_OSERR)
        
        log.debug(purls)

        response = ossindex.callOSSIndex(purls)

        code = audit.auditResults(response)

        _exit(code)

if __name__ == '__main__':
    main()
