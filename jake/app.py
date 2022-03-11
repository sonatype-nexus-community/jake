#!/usr/bin/env python
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
from argparse import ArgumentParser
from datetime import datetime
from typing import Dict

from pyfiglet import figlet_format  # type: ignore
from rich.console import Console

from .command import BaseCommand, jake_version
from .command.iq import IqCommand
from .command.oss import OssCommand
from .command.sbom import SbomCommand

_SUB_COMMANDS: Dict[str, BaseCommand] = {
    'iq': IqCommand(),
    'ddt': OssCommand(),
    'sbom': SbomCommand()
}


class JakeCmd:

    def __init__(self, args: argparse.Namespace) -> None:
        self._arguments = args
        self._console = Console()

        if self._arguments.debug_enabled:
            self._DEBUG_ENABLED = True
            self._debug_message('!!! DEBUG MODE ENABLED !!!')
            self._debug_message('Parsed Arguments: {}'.format(self._arguments))

    @staticmethod
    def get_arg_parser() -> ArgumentParser:
        arg_parser = ArgumentParser(description='Put your Python dependencies in a chokehold')

        # Add global options
        arg_parser.add_argument('-v', '--version', help='show which version of jake you are running',
                                action='version',
                                version=f'jake {jake_version}')
        arg_parser.add_argument('-w', '--warn-only', action='store_true', dest='warn_only',
                                help='prevents exit with non-zero code when issues have been detected')
        arg_parser.add_argument('-X', action='store_true', help='enable debug output', dest='debug_enabled')

        subparsers = arg_parser.add_subparsers(title='Jake sub-commands', dest='cmd', metavar='')
        for subcommand in _SUB_COMMANDS.keys():
            _SUB_COMMANDS[subcommand].setup_argument_parser(
                arg_parser=subparsers.add_parser(
                    name=_SUB_COMMANDS[subcommand].get_argument_parser_name(),
                    help=_SUB_COMMANDS[subcommand].get_argument_parser_help()
                )
            )

        return arg_parser

    def execute(self) -> None:
        # Show the Jake header
        self._print_jake_header()

        # Determine primary command and then hand off to that Command handler
        if self._arguments.cmd and self._arguments.cmd in _SUB_COMMANDS.keys():
            command = _SUB_COMMANDS[self._arguments.cmd]
            exit_code: int = command.execute(arguments=self._arguments)
            exit(exit_code)
        else:
            JakeCmd.get_arg_parser().print_help()

    def _debug_message(self, message: str) -> None:
        if self._DEBUG_ENABLED:
            print('[DEBUG] - {} - {}'.format(datetime.now(), message))

    def _print_jake_header(self) -> None:
        """ Prints the banner, most of the user facing commands start with this """
        self._console.print(figlet_format('Jake', font='isometric4'), style='dark_green')
        self._console.print(figlet_format('..the snake..', font='invita'), style='dark_green')
        print("Jake Version: {}".format(jake_version))
        print('Put your Python dependencies in a chokehold')
        print('')

    @staticmethod
    def _error_and_exit(message: str, exit_code: int = 1) -> None:
        print('[ERROR] - {} - {}'.format(datetime.now(), message))
        exit(exit_code)


def main() -> None:
    parser = JakeCmd.get_arg_parser()
    args = parser.parse_args()
    JakeCmd(args).execute()


if __name__ == "__main__":
    main()
