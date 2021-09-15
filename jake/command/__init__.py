import argparse
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    # Parsed Arguments
    _arguments: argparse.Namespace

    @abstractmethod
    def handle_args(self):
        pass

    def execute(self, arguments: argparse.Namespace):
        self._arguments = arguments
        self.handle_args()

    @abstractmethod
    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        pass
