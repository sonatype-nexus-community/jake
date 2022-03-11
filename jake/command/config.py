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
from argparse import ArgumentParser

from . import BaseCommand


class ConfigCommand(BaseCommand):

    def handle_args(self) -> int:
        pass

    def get_argument_parser_name(self) -> str:
        return 'config'

    def get_argument_parser_help(self) -> str:
        return 'configure jake for OSS Index or Nexus Lifecycle access'

    def setup_argument_parser(self, arg_parser: ArgumentParser) -> None:
        arg_parser.add_argument('oss', help='configure Nexus IQ Server or OSSIndex', nargs='?',
                                choices=('iq', 'oss'))
