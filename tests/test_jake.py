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
import os
import subprocess
from unittest import TestCase

from jake.command import jake_version


class TestJakeCmd(TestCase):

    def test_jake_no_args(self) -> None:
        output = subprocess.check_output('jake', shell=True)
        self.assertTrue('show this help message and exit' in output.decode('utf-8'))

    def test_jake_help(self):
        output = subprocess.check_output('jake -h', shell=True)
        self.assertTrue('show this help message and exit' in output.decode('utf-8'))

    def test_jake_version(self):
        output = subprocess.check_output('jake -v', shell=True)
        self.assertEqual(f'jake {jake_version}', output.decode('utf-8').rstrip(os.linesep))
