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
from jake.iq.iq import IQ
from jake.cyclonedx.generator import CycloneDxSbomGenerator
from jake.parse.parse import Parse
from jake.audit.audit import Audit
from jake.config.config import Config
from jake.config.iq_config import IQConfig

from ._version import __version__

def main():
  """jake entry point"""
  args = __add_parser_args_and_return()
  log = __setup_logger(args.verbose)
  if args.application:
    config = IQConfig()
  else:
    config = Config()

  if args.snake:
    __get_config_from_std_in(config)
  elif args.python:
    config = IQConfig()
    __get_config_from_std_in(config)
  elif args.version:
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
      if args.application:
        __handle_iq_server(args.application, response, log, config)
      else:
        code = audit.audit_results(response)
    else:
      log.error(
          "Something went horribly wrong, please rerun with -VV to see"
          "what happened")
      _exit(EX_OSERR)

    _exit(code)

def __add_parser_args_and_return():
  parser = argparse.ArgumentParser()
  parser.add_argument('run', help='run jake', choices=['ddt'])
  parser.add_argument(
      '-S', '--snake',
      help='set optional jake config',
      action='store_true')
  parser.add_argument(
      '-P', '--python',
      help='set optional jake IQ Server config',
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
      '-A', '--application',
      help="supply an IQ Server Public Application ID"
  )
  parser.add_argument(
      '-C', '--clean', help="wipe out jake cache", action='store_true')

  return parser.parse_args()

def __setup_logger(verbose):
  logging.basicConfig(level=logging.NOTSET)
  log = logging.getLogger('jake')

  if verbose:
    log.setLevel(logging.DEBUG)
  else:
    log.setLevel(logging.ERROR)

  return log

def __handle_iq_server(application_id, response, log, config: Config):
  sbom_gen = CycloneDxSbomGenerator()
  sbom = sbom_gen.create_and_return_sbom(response)
  log.debug(application_id)
  if config.check_if_config_exists('.iq-server-config') is False:
    print("No IQ server config supplied, please run jake ddt -P to set your config")
    _exit(311)
  iq_server = IQ(application_id)
  _id = iq_server.get_internal_application_id_from_iq_server()
  status_url = iq_server.submit_sbom_to_third_party_api(sbom_gen.sbom_to_string(sbom), _id)
  iq_server.poll_for_results(status_url)
  print(
      "Your IQ Server Report is available here: {}".format(iq_server.get_report_url()))
  if iq_server.get_policy_action() is not None:
    print(
        "Your build has failed, please check your IQ Server Report for more information")
    _exit(1)
  else:
    print(
        "All good to go! Smooth sailing for you! No policy violations reported by IQ Server")
    _exit(0)

def __get_config_from_std_in(config: Config):
  result = config.get_config_from_std_in()
  if result is False:
    _exit(EX_OSERR)
  else:
    _exit(0)

if __name__ == '__main__':
  main()
