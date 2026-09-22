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

import json
import os
import subprocess
import tempfile
from argparse import Namespace
from unittest import TestCase

from jake.command import jake_version
from jake.command.oss import OssCommand


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


class TestWhitelist(TestCase):
    """The whitelist file is JSON, and RFC 8259 makes JSON UTF-8.

    Reading it in the interpreter's locale encoding fails wherever that is not
    UTF-8 - a Windows runner, or any machine with a legacy locale - as soon as
    the documented free-text ``reason`` field carries a non-ASCII character.
    """

    def _apply(self, whitelist_bytes: bytes):
        command = OssCommand.__new__(OssCommand)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, 'jake-whitelist.json')
            with open(path, 'wb') as f:
                f.write(whitelist_bytes)
            command._arguments = Namespace(oss_whitelist_json_file=path)

            class _Report:
                def __init__(self) -> None:
                    self.vulnerabilities = [_Vuln('keep-me'), _Vuln('drop-me')]

            class _Vuln:
                def __init__(self, id_: str) -> None:
                    self.id = id_

            reports = [_Report()]
            command._apply_whitelist(reports)
            return [v.id for v in reports[0].vulnerabilities]

    def test_whitelist_with_a_non_ascii_reason_is_applied(self):
        whitelist = {'ignore': [{'id': 'drop-me', 'reason': 'accepté jusqu’au Q2'}]}
        remaining = self._apply(json.dumps(whitelist, ensure_ascii=False).encode('utf-8'))
        self.assertEqual(['keep-me'], remaining)

    def test_whitelist_with_a_plain_ascii_reason_is_applied(self):
        whitelist = {'ignore': [{'id': 'drop-me', 'reason': 'accepted until Q2'}]}
        remaining = self._apply(json.dumps(whitelist).encode('utf-8'))
        self.assertEqual(['keep-me'], remaining)
