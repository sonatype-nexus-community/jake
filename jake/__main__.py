"""jake entry point"""
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name
# pylint: disable=unnecessary-pass
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
from os import _exit, EX_OSERR, path, mkdir
from pathlib import Path

import click
from termcolor import cprint
from pyfiglet import figlet_format
from colorama import init, Fore
from yaspin import yaspin

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

def __print_version(ctx, value):
  if not value:
    return
  print(__package__, 'v' +  __version__)
  ctx.exit()

__shared_options = [
    click.option(
        '-vv', '--verbose',
        is_flag=True,
        default=False,
        help='Set log level to verbose'),
    click.option(
        '-q', '--quiet',
        is_flag=True,
        default=False,
        help='Suppress cosmetic and informational output')
]

def __add_options(options):
  def _add_options(func):
    for option in reversed(options):
      func = option(func)
    return func
  return _add_options

@click.group(help='Jake: Put your python deps in a chokehold.')
@click.option(
    '-v', '--version',
    is_flag=True,
    callback=__print_version,
    expose_value=False,
    is_eager=True,
    help='Print version and exit')
def main():
  """ defining the root cli command as main so that running 'jake'
      in the command line will use this as the entry point
      also prints the banner with every invokation

  Arguments:
      version -- jake flag that will print version and exit
      verbose -- get full runtime output from debug logger
      quiet -- supress the banner TODO: non vulnerable outputs as well
  """
  pass

@main.command()
@click.argument(
    'conf',
    type=click.Choice(['iq', 'ossi']))
def config(conf):
  """Allows a user to set Nexus IQ or OSS Index config params

  Arguments:
      type -- cli input restricted by click to 'iq' and 'ossi'
  """
  cli_config = IQConfig() if conf == 'iq' else Config()

  result = cli_config.get_config_from_std_in()
  if result is False:
    _exit(EX_OSERR)
  else:
    _exit(0)

@main.command()
@__add_options(__shared_options)
@click.option(
    '--clear',
    is_flag=True,
    help='Clear the OSS Index cache')
@click.option(
    '-c', '--conda',
    default=False,
    is_flag=True,
    help='Resolve conda dependencies from std_in')
def ddt(verbose, quiet, clear, conda):
  """SPECIAL MOVE\n
  Allows you to perform scans backed by Sonatype's OSS Index

  Example usage:\n
      Python scan: jake ddt\n
      Conda scan: conda list | jake ddt -c\n
      Clear cache: jake ddt --clear
  """
  if not quiet:
    __banner()

  __setup_logger(verbose)

  oss_index = OssIndex()
  if clear:
    if oss_index.clean_cache():
      print('Cache Cleared')
    _exit(0)

  with yaspin(text="Loading", color="yellow") as spinner:
    spinner.text = "Collecting Dependencies"
    coords = Parse().get_dependencies_from_stdin(sys.stdin) if conda else Pip().get_dependencies()
    spinner.ok("✅ ")

  with yaspin(text="Loading", color="yellow") as spinner:
    spinner.text = "Querying OSS Index"

    response = oss_index.call_ossindex(coords)

    if response is None:
      spinner.fail("💥 ")
      click.echo(
          "Something went horribly wrong, there is no response from OSS Index",
          "please rerun with -VV to see what happened")
      _exit(EX_OSERR)
    spinner.ok("✅ ")

  with yaspin(text="Loading", color="yellow") as spinner:
    spinner.text = "Auditing results from OSS Index"
    audit = Audit()
    spinner.ok("✅ ")
    code = audit.audit_results(response)
    _exit(code)

@main.command()
@__add_options(__shared_options)
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
@click.option(
    '-c', '--conda',
    default=False,
    is_flag=True,
    help='Resolve conda dependencies from std_in')
def iq(verbose, quiet, application, stage, user, password, host, conda):
  """EXTRA SPECIAL MOVE\n
  Allows you to perform scans backed by Sonatype's Nexus IQ Server

  Example usage:\n
      Python scan: jake iq -a <AppId>\n
      Conda scan: conda list | jake iq -a <AppId> -c\n

  Will pull values for other params from config unless overwritten here\n

      To set the IQ config: jake config iq\n
  """
  if not quiet:
    __banner()

  __setup_logger(verbose)

  iq_args = {}
  iq_args['application'] = application
  iq_args['stage'] = stage
  iq_args['user'] = user
  iq_args['password'] = password
  iq_args['host'] = host

  with yaspin(text="Loading", color="yellow") as spinner:
    spinner.text = "Collecting Dependencies"
    coords = Parse().get_dependencies_from_stdin(sys.stdin) if conda else Pip().get_dependencies()
    spinner.text = "Calling OSS Index"
    response = OssIndex().call_ossindex(coords)
    spinner.ok("✅ ")

    __handle_iq_server(response, iq_args)

  # if args.application:
  #    coords.join_coords(Pip().get_dependencies().get_coordinates())


def __setup_logger(verbose):
  logger = logging.getLogger('jake')
  logger.setLevel(logging.DEBUG)

  home = str(Path.home())
  if not path.exists(path.join(home, '.ossindex')):
    mkdir(path.join(home, '.ossindex'))

  filepath = path.join(home, '.ossindex', 'jake.combined.log')
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

  fh = logging.FileHandler(filepath)

  logger.addHandler(fh)

  ch = logging.StreamHandler()

  if verbose:
    ch.setLevel(logging.DEBUG)
  else:
    ch.setLevel(logging.ERROR)

  fh.setFormatter(formatter)
  ch.setFormatter(formatter)

  logger.addHandler(ch)

def __handle_iq_server(response, args):
  with yaspin(text="Loading", color="yellow") as spinner:
    spinner.text = "Calling Nexus IQ Server"
    sbom_gen = CycloneDxSbomGenerator()
    sbom = sbom_gen.create_and_return_sbom(response)
    iq_requests = IQ(args)
    _id = iq_requests.get_internal_id()
    status_url = iq_requests.submit_sbom_to_third_party_api(
        sbom_gen.sbom_to_string(sbom), _id)
    iq_requests.poll_for_results(status_url)
    if iq_requests.get_policy_action() is not None:
      spinner.fail("💥 ")
      print(Fore.YELLOW +
            "Your IQ Server Report is available here: {}".format(iq_requests.get_report_url()))
      print(Fore.YELLOW +
            "Your build has failed, please check your IQ Server Report for more information")
      _exit(1)
    else:
      spinner.ok("✅ ")
      print(Fore.GREEN +
            "Your IQ Server Report is available here: {}".format(iq_requests.get_report_url()))
      print(Fore.GREEN +
            "All good to go! Smooth sailing for you! No policy violations reported by IQ Server")
      _exit(0)

def __banner():
  top_font = 'isometric4' # another option: 'isometric1'
  bot_font = 'invita'
  top = 'Jake'
  bot = ' ..the snake..'
  cprint(figlet_format(top, font=top_font), 'green', attrs=[])
  cprint(figlet_format(bot, font=bot_font), 'blue', attrs=['dark'])
  click.echo("Jake version: v{}".format(__version__))
  click.echo('Put your python deps in a chokehold.')

if __name__ == '__main__':
  main()
