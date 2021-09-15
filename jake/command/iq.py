import argparse
from . import BaseCommand


class IqCommand(BaseCommand):

    def handle_args(self):
        pass

    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        parser: argparse.ArgumentParser = subparsers.add_parser('iq', help='perform a scan backed by Nexus Lifecycle')

        parser.add_argument('-s', '--server-url', help='Full http(s):// URL to your Nexus Lifecycle server',
                            metavar='https://localhost:8070', required=True, dest='iq_server_url')

        parser.add_argument('-i', '--application-id', help='Public Application ID in Nexus Lifecycle',
                            metavar='APP_ID', required=True, dest='iq_application_id')

        parser.add_argument('-u', '--username', help='Username for authentication to Nexus Lifecycle',
                            metavar='USER_ID', required=True, dest='iq_username')

        parser.add_argument('-p', '--password', help='Password for authentication to Nexus Lifecycle',
                            metavar='PASSWORD', required=True, dest='iq_password')

