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

from setuptools import setup, find_packages

from jake._version import __version__

with open("README.md", "r", encoding="utf8") as fh:
  LONG_DESCRIPTION = fh.read()

with open('requirements.txt') as requirements:
  REQUIRED = requirements.read().splitlines()

setup(
    name='jake',
    version=__version__,
    url="https://github.com/sonatype-nexus-community/jake",
    author="Sonatype Community",
    author_email="community-group@sonatype.com",
    description="An OSS Index integration to check for vulnerabilities in your Conda environments",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    packages=find_packages(exclude=["jake/tests/*", "jake/tests/"]),
    python_requires='>=3.6',
    package_data={
        'jake':
            ['cyclonedx/v1_1/*.xsd']
    },
    install_requires=REQUIRED,
    entry_points={
        'console_scripts':
            ['jake=jake.__main__:main']
    }
)
