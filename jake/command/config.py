import argparse
from . import BaseCommand


class ConfigCommand(BaseCommand):

    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        parser_config: argparse.ArgumentParser = subparsers.add_parser(
            'config',
            help='configure jake for OSS Index or Nexus Lifecycle access'
        )

        parser_config.add_argument('oss', help='configure Nexus IQ Server or OSSIndex', nargs='?',
                                   choices=('iq', 'oss'))
