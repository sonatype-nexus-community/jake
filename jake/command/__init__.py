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
import sys
from abc import ABC, abstractmethod
from typing import Optional

if sys.version_info >= (3, 8):
    from importlib.metadata import version as meta_version
else:
    from importlib_metadata import version as meta_version

try:
    jake_version: Optional[str] = str(meta_version('jake'))  # type: ignore[no-untyped-call]
except Exception:
    jake_version = 'DEVELOPMENT'


class BaseCommand(ABC):
    # Parsed Arguments
    _arguments: argparse.Namespace

    @abstractmethod
    def handle_args(self) -> int:
        pass

    def execute(self, arguments: argparse.Namespace) -> int:
        self._arguments = arguments
        return self.handle_args()

    @abstractmethod
    def setup_argument_parser(self, subparsers: argparse._SubParsersAction) -> None:
        pass
