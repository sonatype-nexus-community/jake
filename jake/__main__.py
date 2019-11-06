"""jake entry point"""
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

from os import _exit, EX_OSERR

from jake.ossindex.ossindex import OssIndex
from jake.parse.parse import Parse
from jake.audit.audit import Audit
from jake.config.config import Config

from ._version import __version__


def main():
  """jake entry point"""
  parser = argparse.ArgumentParser()
  parser.add_argument('run', help='run jake', choices=['ddt'])
  parser.add_argument(
      '-S', '--snake',
      help='set optional jake config',
      action='store_true')
  parser.add_argument(
      '-V', '--version',
      help='show program version and exit',
      action='store_true')
  parser.add_argument(
      '-VV', '--verbose',
      help="set verbosity level to debug",
      action='store_true')
  parser.add_argument(
      '-C', '--clean', help="wipe out jake cache", action='store_true')
  args = parser.parse_args()
  logging.basicConfig(level=logging.NOTSET)
  log = logging.getLogger('jake')

  if args.snake:
    config = Config()
    result = config.get_config_from_std_in()
    if result is False:
      _exit(OSError)
    else:
      _exit(0)

  if args.verbose:
    log.setLevel(logging.DEBUG)
  else:
    log.setLevel(logging.ERROR)

  if args.version:
    print(__version__)
    _exit(0)

  parse = Parse()
  ossindex = OssIndex()
  audit = Audit()

  if args.clean:
    ossindex.clean_cache()

  if args.run == 'ddt':
    log.info('Calling OSS Index')
    purls = parse.get_dependencies_from_stdin(sys.stdin)
    if purls is None:
      log.error(
          "No purls returned, ensure that conda list is returning"
          "a list of dependencies")
      _exit(EX_OSERR)

    log.debug("Total purls: %s", len(purls.get_coordinates()))

    response = ossindex.call_ossindex(purls)
    if response is not None:
      code = audit.audit_results(response)
    else:
      log.error(
          "Something went horribly wrong, please rerun with -VV to see"
          "what happened")
      _exit(EX_OSERR)

    _exit(code)


if __name__ == '__main__':
  main()
