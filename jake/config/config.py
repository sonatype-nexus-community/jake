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

class Config(object):
  def __init__(self, save_location=''):
    self._log = logging.getLogger('jake')
    self._username = ""
    self._password = ""
    if save_location != '':
      self._save_location = save_location
    else:
      self._save_location = str(Path.home())

  def setPassword(self, password):
    self._password = password
  
  def setUsername(self, username):
    self._username = username

  def getConfigFromStdIn(self):
    username = input("Please enter your email address for your OSS Index account: ")
    password = input("Please enter your API Key for OSS Index: ")

    self.setUsername(username)
    self.setPassword(password)

    result = self.saveConfigToFile()
    
    return result

  def saveConfigToFile(self):
    try:
      with open(self._save_location + "/.jake-config","w+") as f:
        f.write("Username: " + self._username + "\n")
        f.write("Password: " + self._password + "\n")
        return True
    except Exception as e:
      self._log.error("Uh oh, an error happened: %s", str(e))
      return False

  def getConfigFromFile(self):
    with open(self._save_location + "/.jake-config") as f:
      for line in f.readlines():
        lineArray = line.split(" ")
        if lineArray[0] == 'Username:':
          username = str(lineArray[1]).rstrip()
        elif lineArray[0] == 'Password:':
          password = str(lineArray[1]).rstrip()

    return (username, password)

  def checkIfConfigExists(self):
      config_location = Path(self._save_location + "/.jake-config")
      return config_location.exists()