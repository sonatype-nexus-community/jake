"""config.py stores OSSIndex credentials"""
# Copyright 2019 Sonatype Inc.
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
import logging
import os

from pathlib import Path

class Config():
  """config.py handles getting credentials for OSSIndex or setting them"""
  def __init__(self, save_location=''):
    self._log = logging.getLogger('jake')

    self._config_name = '.oss-index-config'
    self._old_config_name = '.jake-config'

    self._username = ""
    self._password = ""

    if save_location != '':
      self._save_location = save_location
    else:
      self._save_location = str(Path.home())

    self.__migrate_config_if_at_jake_location()

  def set_password(self, password):
    """set password for OSSIndex request"""
    self._password = password

  def set_username(self, username):
    """set username for OSSIndex request"""
    self._username = username

  def get_config_from_std_in(self):
    """requests user to input their username and password from stdin"""
    username = input("Please enter your username for your OSS Index account: ")
    password = input("Please enter your API Key for OSS Index: ")

    self.set_username(username)
    self.set_password(password)

    result = self.save_config_to_file(
        {"Username": self._username,
         "Password": self._password},
        self._config_name)

    return result

  def save_config_to_file(self, fields, config_name):
    """save stdin to save_location/.oss-index-config or .iq-server-config"""
    try:
      with open(os.path.join(self._save_location, config_name), "w+") as file:
        for key, value in fields.items():
          file.write("{}: {}\n".format(key, value))
        return True
    except FileNotFoundError as exception:
      self._log.error("Uh oh, an error happened: %s", str(exception))
      return False

  def get_config_from_file(self, fields, config_name):
    """get credentials from save_location/.jake-config"""
    with open(os.path.join(self._save_location, config_name)) as file:
      results = {}
      for line in file.readlines():
        line_array = line.split(" ")
        for key in fields:
          if line_array[0].rstrip(":") == key:
            results[key] = str(line_array[1]).rstrip()

    return results

  def check_if_config_exists(self, config_location='.oss-index-config'):
    """check to see if config exists at save_location/config_location"""
    config_location = Path(os.path.join(self._save_location, config_location))
    return config_location.exists()

  def __migrate_config_if_at_jake_location(self):
    """check to see if save_location/.jake-config exists, if so migrate to
    .oss-index-config"""
    if self.check_if_config_exists(self._old_config_name):
      self._log.debug("Migrating OSS Index config")
      os.rename(os.path.join(self._save_location, self._old_config_name),
                os.path.join(self._save_location, self._config_name))
    else:
      self._log.debug("No need to migrate config")
