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

from cyclonedx.model.bom import Bom
from cyclonedx.output import BaseOutput, get_instance, OutputFormat, SchemaVersion, DEFAULT_SCHEMA_VERSION
from cyclonedx.parser import BaseParser
from cyclonedx.parser.environment import EnvironmentParser
from cyclonedx.parser.pipenv import PipEnvFileParser
from cyclonedx.parser.poetry import PoetryFileParser
from cyclonedx.parser.requirements import RequirementsFileParser
from . import BaseCommand


class SbomCommand(BaseCommand):

    def handle_args(self) -> int:
        self._arguments.sbom_input_type
        bom = Bom.from_parser(self._get_parser())

        output_format = OutputFormat.XML
        if self._arguments.sbom_output_format == 'json':
            output_format = OutputFormat.JSON

        schema_version = DEFAULT_SCHEMA_VERSION
        if self._arguments.sbom_schema_version:
            schema_version = SchemaVersion['V{}'.format(str(self._arguments.sbom_schema_version).replace('.', '_'))]

        output: BaseOutput = get_instance(bom=bom, output_format=output_format, schema_version=schema_version)

        if self._arguments.sbom_output_file:
            # Output to a file
            output.output_to_file(filename=self._arguments.sbom_output_file, allow_overwrite=True)
        else:
            # Output to STDOUT
            print(output.output_as_string())

        return 0

    def setup_argument_parser(self, subparsers: argparse._SubParsersAction):
        parser: argparse.ArgumentParser = subparsers.add_parser(
            'sbom',
            help='generate a CycloneDX software-bill-of-materials (no vulnerabilities)',
        )

        parser.add_argument('-it', '--input-type',
                            help='how jake should find the packages from which to generate your SBOM.'
                                 'ENV = Read from the current Python Environment; PIP = read from a requirements.txt; '
                                 'PIPENV = read from Pipfile.lock; POETRY = read from a poetry.lock. '
                                 '(Default = ENV)',
                            metavar='TYPE', choices={'ENV', 'PIP', 'PIPENV', 'POETRY'}, default='ENV',
                            dest='sbom_input_type')
        parser.add_argument('-o', '--output-file', help='Specify a file to output the SBOM to', metavar='PATH/TO/FILE',
                            dest='sbom_output_file')
        parser.add_argument('--output-format', help='SBOM output format (default = xml)', choices={'json', 'xml'},
                            default='xml', dest='sbom_output_format')
        parser.add_argument('--schema-version', help='CycloneDX schema version to use (default = 1.3)',
                            choices={'1.3', '1.2', '1.1', '1.0'}, default='1.3',
                            dest='sbom_schema_version')

    def _get_parser(self) -> BaseParser:
        if self._arguments.sbom_input_type == 'ENV':
            return EnvironmentParser()

        if self._arguments.sbom_input_type == 'PIP':
            return RequirementsFileParser(requirements_file='requirements.txt')

        if self._arguments.sbom_input_type == 'PIPENV':
            return PipEnvFileParser(pipenv_lock_filename='Pipfile.lock')

        if self._arguments.sbom_input_type == 'POETRY':
            return PoetryFileParser(poetry_lock_filename='poetry.lock')

        raise NotImplementedError
