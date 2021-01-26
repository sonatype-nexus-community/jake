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

"""test_main.py test stuff in __main__.py"""
import unittest

from yaspin import yaspin

from jake.__main__ import _show_summary
from jake.iq.iq import IQ


class TestMain(unittest.TestCase):
  """TestMain tests stuff in __main__"""

  def setUp(self):
    iq_args = {}
    self.func = IQ(args=iq_args)

  def test_show_summary(self):
    """test_show_summary verifies exit code is correct for a given IQ Policy Action"""
    spinner = yaspin(text="Loading", color="magenta")

    # pylint: disable=W0212
    self.func._report_url = 'myRelativeReportURL'

    self.func._policy_action = None
    self.assertEqual(3, _show_summary(self.func, spinner))

    self.func._policy_action = "Failure"
    self.assertEqual(1, _show_summary(self.func, spinner))

    self.func._policy_action = "Warning"
    self.assertEqual(0, _show_summary(self.func, spinner))

    self.func._policy_action = "None"
    self.assertEqual(0, _show_summary(self.func, spinner))
