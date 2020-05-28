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

"""iq_config.py stores IQ credentials"""
from ..config.config import Config

class IQConfig(Config):
  """does IQ specific config setting and retrieval"""
  def __init__(self, save_location=''):
    super().__init__('.iqserver', save_location)
    self._iq_server_config_name = '.iq-server-config'
    self._iq_server_location = ''

  def get_config_from_std_in(self):
    """requests user to input their username and password from stdin"""
    username = input("Please enter your username for your IQ Server account: ")
    password = input("Please enter your user token for IQ Server: ")
    iq_server_location = input("Please provide the location of your IQ Server: ")
    self._iq_server_location = iq_server_location.rstrip("/")
    self.set_username(username)
    self.set_password(password)

    result = self.save_config_to_file(
        {"Username": self._username,
         "Token": self._password,
         "Server": self._iq_server_location},
        self._iq_server_config_name)

    return result
