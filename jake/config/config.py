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

from pathlib import Path

class Config():
  """config.py handles getting credentials for OSSIndex or setting them"""
  def __init__(self, save_location=''):
    self._log = logging.getLogger('jake')
    self._username = ""
    self._password = ""
    if save_location != '':
      self._save_location = save_location
    else:
      self._save_location = str(Path.home())

  def set_password(self, password):
    """set password for OSSIndex request"""
    self._password = password

  def set_username(self, username):
    """set username for OSSIndex request"""
    self._username = username

  def get_config_from_std_in(self):
    """requests user to input their username and password from stdin"""
    username = input(
        "Please enter your email address for your OSS Index account: ")
    password = input("Please enter your API Key for OSS Index: ")

    self.set_username(username)
    self.set_password(password)

    result = self.save_config_to_file()

    return result

  def save_config_to_file(self):
    """save stdin to save_location/.jake-config"""
    try:
      with open(self._save_location + "/.jake-config", "w+") as file:
        file.write("Username: " + self._username + "\n")
        file.write("Password: " + self._password + "\n")
        return True
    except FileNotFoundError as exception:
      self._log.error("Uh oh, an error happened: %s", str(exception))
      return False

  def get_config_from_file(self):
    """get credentials from save_location/.jake-config"""
    with open(self._save_location + "/.jake-config") as file:
      for line in file.readlines():
        line_array = line.split(" ")
        if line_array[0] == 'Username:':
          username = str(line_array[1]).rstrip()
        elif line_array[0] == 'Password:':
          password = str(line_array[1]).rstrip()

    return (username, password)

  def check_if_config_exists(self):
    """check to see if save_location/.jake-config exists"""
    config_location = Path(self._save_location + "/.jake-config")
    return config_location.exists()
