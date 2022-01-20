#!/usr/bin/env python
# encoding: utf-8

#
# Copyright 2019-Present Sonatype Inc.
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
#

import argparse
from datetime import datetime
from typing import Dict

from pyfiglet import figlet_format
from rich.console import Console

from .command import BaseCommand, _jake_version
from .command.iq import IqCommand
from .command.oss import OssCommand
from .command.sbom import SbomCommand


class JakeCmd:
    # Whether debug output is enabled
    _DEBUG_ENABLED: bool = False

    # Argument Parser
    _arg_parser: argparse.ArgumentParser

    # Parsed Arguments
    _arguments: argparse.Namespace

    # Sub Commands
    _subcommands: Dict[str, BaseCommand] = []

    # Rich Console
    _console: Console

    def __init__(self):
        self._console = Console()

        # Build and parse command arguments
        self._load_subcommands()
        self._build_arg_parser()
        self._parse_arguments()

        if self._arguments.debug_enabled:
            self._DEBUG_ENABLED = True
            self._debug_message('!!! DEBUG MODE ENABLED !!!')
            self._debug_message('Parsed Arguments: {}'.format(self._arguments))

    def execute(self):
        # Show the Jake header
        self._print_jake_header()

        # Determine primary command and then hand off to that Command handler
        if self._arguments.cmd:
            command = self._subcommands[self._arguments.cmd]
            exit_code: int = command.execute(arguments=self._arguments)
            exit(exit_code)
        else:
            self._arg_parser.print_help()

    def _load_subcommands(self):
        self._subcommands = {
            # 'config': ConfigCommand(),
            'iq': IqCommand(),
            'ddt': OssCommand(),
            'sbom': SbomCommand()
        }

    def _build_arg_parser(self):
        self._arg_parser = argparse.ArgumentParser(description='Put your Python dependencies in a chokehold')

        # Add global options
        self._arg_parser.add_argument('-v', '--version', help='show which version of jake you are running',
                                      action='version',
                                      version=f'jake {_jake_version}')
        self._arg_parser.add_argument('-w', '--warn-only', action='store_true', dest='warn_only',
                                      help='prevents exit with non-zero code when issues have been detected')
        self._arg_parser.add_argument('-X', action='store_true', help='enable debug output', dest='debug_enabled')

        subparsers = self._arg_parser.add_subparsers(title='Jake sub-commands', dest='cmd', metavar='')
        for subcommand in self._subcommands.keys():
            self._subcommands[subcommand].setup_argument_parser(subparsers=subparsers)

    def _debug_message(self, message: str):
        if self._DEBUG_ENABLED:
            print('[DEBUG] - {} - {}'.format(datetime.now(), message))

    def _print_jake_header(self):
        """ Prints the banner, most of the user facing commands start with this """
        self._console.print(figlet_format('Jake', font='isometric4'), style='dark_green')
        self._console.print(figlet_format('..the snake..', font='invita'), style='dark_green')
        print("Jake Version: {}".format(_jake_version))
        print('Put your Python dependencies in a chokehold')
        print('')

    @staticmethod
    def _error_and_exit(message: str, exit_code: int = 1):
        print('[ERROR] - {} - {}'.format(datetime.now(), message))
        exit(exit_code)

    def _parse_arguments(self):
        self._arguments = self._arg_parser.parse_args()


# only for testing
def _create_cmd():
    return JakeCmd()


def main():
    JakeCmd().execute()


if __name__ == "__main__":
    main()
