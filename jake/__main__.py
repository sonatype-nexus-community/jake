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

from os import _exit, EX_OSERR
import sys
import logging
import click
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init
from jake.ossindex.ossindex import OssIndex
from jake.iq.iq import IQ
from jake.cyclonedx.generator import CycloneDxSbomGenerator
from jake.parse.parse import Parse
from jake.pip.pip import Pip
from jake.audit.audit import Audit
from jake.config.config import Config
from jake.config.iq_config import IQConfig
from jake._version import __version__

init(strip=not sys.stdout.isatty()) # strip colors on redirected output

@click.group(help='Jake: Put your python deps in a chokehold.')
@click.option(
    '-V', '--version',
    is_flag=True,
    callback=__print_version,
    expose_value=False,
    is_eager=True,
    help='Print version and exit')
@click.option(
    '-VV', '--verbose',
    is_flag=True,
    default=False,
    help='Set log level to verbose')
@click.option(
    '-Q', '--quiet',
    is_flag=True,
    default=False,
    help='Suppress cosmetic and informational output')
def main(verbose, quiet):
  """ defining the root cli command as main so that running 'jake'
      in the command line will use this as the entry point
      also prints the banner with every invokation

  Arguments:
      version -- jake flag that will print version and exit
      verbose -- get full runtime output from debug logger
      quiet -- supress the banner TODO: non vulnerable outputs as well
  """
  if not quiet:
    __banner()
  pass

@main.command()
@click.argument(
    'type',
    type=click.Choice(['iq', 'ossi']))
def config(type):
  """ subcommand to prompt the user to set iq or ossi config params

  Arguments:
      type -- cli input restricted by click to 'iq' and 'ossi'
  """
  config = IQConfig() if type == 'iq' else Config()

  # call the config entry prompt and exit
  result = config.get_config_from_std_in()
  _exit(EX_OSERR) if result is False else _exit(0)

@main.command()
@click.option(
    '--clear',
    is_flag=True,
    help='Clear the OSS Index cache')
@click.option(
    '-c', '--conda',
    default=False,
    is_flag=True,
    help='Resolve conda dependencies from std_in')
def ddt(clear, conda):
  """ SPECIAL MOVE
      handles args and program flows unique to an OSS Index scan

  Arguments:
      clear -- flag to clear the cache
      conda -- flag to resolve conda dependencies piping conda list from std_in
  """
  coords = Parse().get_dependencies_from_stdin(sys.stdin) if conda else Pip().get_dependencies()

  oss_index = OssIndex()
  response = oss_index.call_ossindex(coords)

  if response is None:
    click.echo(
        "Something went horribly wrong, there is no response from OSS Index",
        "please rerun with -VV to see what happened")
    _exit(EX_OSERR)

  audit = Audit()
  code = audit.audit_results(response)

  if clear:
    if oss_index.clean_cache():
      print('Cache Cleared')
    _exit(code)

@main.command()
@click.option(
    '-a', '--application',
    help='Supply an IQ Server Public Application ID',
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

  coords = Pip().get_dependencies()
  response = OssIndex().call_ossindex(coords)
  __handle_iq_server(response, iq_args)

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

  log.setLevel(logging.DEBUG) if verbose else log.setLevel(logging.ERROR)

  return log

def __handle_iq_server(response, args):
  sbom_gen = CycloneDxSbomGenerator()
  sbom = sbom_gen.create_and_return_sbom(response)
  iq_requests = IQ(args)
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

def __banner():
  top_font = 'isometric4' # another option: 'isometric1'
  bot_font = 'invita'
  # version_font = 'digital'
  top = 'Jake'
  bot = ' ..the snake..'
  # version = 'v' + __version__
  cprint(figlet_format(top, font=top_font), 'green', attrs=[])
  cprint(figlet_format(bot, font=bot_font), 'blue', attrs=['dark'])
  # cprint(figlet_format(version, font=version_font), 'white', attrs=[])
  click.echo('Put your python deps in a chokehold.')
  # 'on_blue' after the primary color to set background

def __print_version(ctx, value):
  if not value:
    return
  print(__package__, 'v' +  __version__)
  ctx.exit()

if __name__ == '__main__':
  main()
