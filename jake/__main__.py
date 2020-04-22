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
from jake.pip.pip import Pip
from jake.audit.audit import Audit
from jake.config.config import Config
from jake.config.iq_config import IQConfig

from jake._version import __version__

import click

@click.group()
@click.option(
  '-V', '--version',
  is_flag=True,
  default=False,
  help='Print version and exit')
@click.option(
  '-VV', '--verbose',
  is_flag=True,
  default=False,
  help='Set log level to verbose')
def main(version, verbose):
      if version:
            print(__package__, 'v' +  __version__)
            _exit(0)
      pass

@main.command()
@click.argument(
  'type',
  type=click.Choice(['iq', 'ossi']))
def config(type):
      if type == 'iq':
            config = IQConfig()
      else:
            config = Config()
      result = config.get_config_from_std_in()
      if result is False:
            _exit(EX_OSERR)
      else:
            _exit(0)

@main.command()
@click.option(
  '-a', '--application',
  help='supply an IQ Server Public Application ID',
  required=True)
@click.option(
  '-s', '--stage',
  default='develop',
  type=click.Choice(['develop', 'build', 'stage-release', 'release']),
  help='Specify a stage')
@click.option(
  '-u', '--user',
  help='Set username for Sonatype IQ')
@click.option(
  '-p', '--password',
  help='Set password or token for associated user')
@click.option(
  '-h', '--host',
  help='Specify an endpoint for Sonatype IQ')
def iq(application, stage, user, password, host):
      iq_args = {}
      iq_args['application'] = application
      iq_args['stage'] = stage
      iq_args['user'] = user
      iq_args['password'] = password
      iq_args['host'] = host
      print(iq_args)

class ArgRouter():
      def __init__(self, verbose, snek):
            click.echo('in ArgRouter', verbose, snek)
class ArgRouterOld():
  """
  Encapsulates all parsing and subparsing of command line args

  Initalizing ArgRouter() will parse all args present in sys_in and generate the args list

  Public function get_args() returns the args list after init
  """

  def __init__(self):
    self._parser = argparse.ArgumentParser(
        description='Jake: Put your python deps in a chokehold'
    )
    # defines the positional argument where a sub-command would be
    self._sub_parsers = self._parser.add_subparsers(
        help='Select sub-command to run',
        dest='command'
    )

    # picks up flags that can be passed in regardless of the sub-command
    self.__parse_jake_args()

    # create a nested parser in the root parser for each valid sub-command
    config_parser = self._sub_parsers.add_parser('config')
    ossi_parser = self._sub_parsers.add_parser('ddt')
    iq_parser = self._sub_parsers.add_parser('iq')

    # looks for an iq or ossi value after the config sub-command
    config_parser.add_argument(
        'type',
        help='set config type',
        choices=['iq', 'ossi'])

    # looks for the app-id flag after the iq sub-command
    iq_parser.add_argument(
        '-a', '--application',
        help='supply an IQ Server Public Application ID',
        required=True)
    # App stage, a develop throw-away report by default
    iq_parser.add_argument(
        '-s', '--stage',
        help='specify a stage',
        default='develop',
        choices=['develop', 'build', 'stage-release', 'release'])
    # Username, not required, config param
    iq_parser.add_argument(
        '-u', '--user',
        help='specify a username for Sonatype IQ')
    # Password or token, not required, config param
    iq_parser.add_argument(
        '-p', '--password',
        help='specify a password/token for Sonatype IQ')
    # IQ Endpoint, not required, config param
    iq_parser.add_argument(
        '-e', '--host',
        help='specify an endpoint for Sonatype IQ')

    # The cache is oss index specific, except IQ uses ossindex, jake arg?
    ossi_parser.add_argument(
        '-C', '--clean',
        help='wipe out jake cache',
        action='store_true')

    # Resolves all the args, including sub-command args
    self._args = self._parser.parse_args()

  def __parse_jake_args(self):
      """parses command line flags from the jake root command, can always pass these in"""
      self._parser.add_argument(
          '-N', '--snek',
          help='get python requirements instead',
          action='store_true')
      self._parser.add_argument(
          '-VV', '--verbose',
          help="set verbosity level to debug",
          action='store_true')
      self._parser.add_argument(
          '-V', '--version',
          help='show version and exit',
          action='store_true'
      )

  def get_args(self):
      """
      args list getter

      returns the args list that gets generated on init

      type: argparse.Namespace object that can be cast as a dict w/ var(args)
      """
      return self._args


def old_main():
  """jake entry point"""
  router = ArgRouter()
  args = router.get_args()
  log = __setup_logger(args.verbose)

  if args.version:
    print(__version__)
    _exit(0)

  if args.command == 'config':
    if args.type == 'iq':
      config = IQConfig()
    else:
      config = Config()
    result = config.get_config_from_std_in()
    if result is False:
      _exit(EX_OSERR)
    else:
      _exit(0)

  if args.snek:
    pip_handler = Pip()
    coords = pip_handler.get_dependencies()
  else:
    parse = Parse()
    coords = parse.get_dependencies_from_stdin(sys.stdin)

  if coords is None:
    log.error(
        "No purls returned, ensure that conda list is returning"
        "a list of dependencies")
    _exit(EX_OSERR)

  log.debug("Total purls: %s", len(coords.get_coordinates()))

  oss_index = OssIndex()
  ossi_response = oss_index.call_ossindex(coords)

  if ossi_response is None:
    log.error(
        "Something went horribly wrong, there is no response from Oss Index",
        "please rerun with -VV to see what happened")
    _exit(EX_OSERR)

  if args.command == 'iq':
    __handle_iq_server(ossi_response, args, log),

  if args.command == 'ossi':
    audit = Audit()
    code = audit.audit_results(ossi_response)
    if args.clean:
      if oss_index.clean_cache():
        print('Cache Cleared')
    _exit(code)

  # TODO: determine if joining conda and pypi purls for hybridized IQ results is feasible
  # This joins the pypi coordinates from pkg_resources and the conda coordinates from conda
  # list and will generate a report with dupes.  I would remove the conda purls that have dupes
  # from the pypi purls, but not all of the pypi purls get results in IQ and it would be difficult
  # to figure out which ones will aheadof time (before making the request)

  # if args.application:
  #    coords.join_coords(Pip().get_dependencies().get_coordinates())


def __setup_logger(verbose):
  logging.basicConfig(level=logging.NOTSET)
  log = logging.getLogger('jake')

  if verbose:
    log.setLevel(logging.DEBUG)
  else:
    log.setLevel(logging.ERROR)

  return log


def __handle_iq_server(response, args, log):
  sbom_gen = CycloneDxSbomGenerator()
  sbom = sbom_gen.create_and_return_sbom(response)
  log.debug(args.application)
  iq_requests = IQ(args, log)
  _id = iq_requests.get_internal_id()
  status_url = iq_requests.submit_sbom_to_third_party_api(
      sbom_gen.sbom_to_string(sbom), _id)
  iq_requests.poll_for_results(status_url)
  print(
      "Your IQ Server Report is available here: {}".format(iq_requests.get_report_url()))
  if iq_requests.get_policy_action() is not None:
    print(
        "Your build has failed, please check your IQ Server Report for more information")
    _exit(1)
  else:
    print(
        "All good to go! Smooth sailing for you! No policy violations reported by IQ Server")
    _exit(0)


if __name__ == '__main__':
  main()
