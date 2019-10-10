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
import logging
import json

from conda.cli.python_api import Commands, run_command
from os import _exit, EX_OSERR

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse

def main():
    log = logging.getLogger('jake')
    log.setLevel(logging.DEBUG)

    parse = Parse()
    ossindex = OssIndex()

    log.debug('Getting arguments')
    args = sys.argv[1:]

    for arg in args:
        log.debug(arg)
        if arg == 'ddt':
            log.info('Calling OSS Index')

            purls = parse.getDependencies(run_command_list=run_command(Commands.LIST, "-n root"))
            if purls is None:
                log.error("No purls returned, likely culprit is no Conda installed")
                _exit(EX_OSERR)
            
            log.debug(purls)

            response = ossindex.callOSSIndex(purls)
            log.debug(response.json())

if __name__ == '__main__':
    main()
