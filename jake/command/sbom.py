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
import sys
from argparse import ArgumentParser, FileType

import cyclonedx.parser
from cyclonedx.model import ExternalReference, ExternalReferenceType, Tool, XsUri
from cyclonedx.model.bom import Bom
from cyclonedx.output import BaseOutput, get_instance, OutputFormat, SchemaVersion, LATEST_SUPPORTED_SCHEMA_VERSION
from cyclonedx_py.parser.conda import CondaListJsonParser, CondaListExplicitParser
from cyclonedx_py.parser.environment import EnvironmentParser
from cyclonedx_py.parser.pipenv import PipEnvParser, PipEnvFileParser
from cyclonedx_py.parser.poetry import PoetryParser, PoetryFileParser
from cyclonedx_py.parser.requirements import RequirementsParser, RequirementsFileParser

from . import BaseCommand, jake_version

ThisTool = Tool(vendor='Sonatype Nexus Community', name='jake', version=jake_version or 'UNKNOWN')
ThisTool.external_references.update([
    ExternalReference(
        reference_type=ExternalReferenceType.BUILD_SYSTEM,
        url=XsUri('https://app.circleci.com/pipelines/github/sonatype-nexus-community/jake')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.DISTRIBUTION,
        url=XsUri('https://pypi.org/project/jake/')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.ISSUE_TRACKER,
        url=XsUri('https://github.com/sonatype-nexus-community/jake/issues')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.LICENSE,
        url=XsUri('https://github.com/sonatype-nexus-community/jake/blob/main/LICENSE')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.RELEASE_NOTES,
        url=XsUri('https://github.com/sonatype-nexus-community/jake/blob/main/CHANGELOG.md')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.VCS,
        url=XsUri('https://github.com/sonatype-nexus-community/jake')
    ),
    ExternalReference(
        reference_type=ExternalReferenceType.WEBSITE,
        url=XsUri('https://www.sonatype.com/products/free-developer-tools')
    )
])


class SbomCommand(BaseCommand):

    def handle_args(self) -> int:
        bom = Bom.from_parser(parser=self._get_parser())
        bom.metadata.tools.add(ThisTool)

        output_format = OutputFormat.XML
        if self.arguments.sbom_output_format == 'json':
            output_format = OutputFormat.JSON

        schema_version = LATEST_SUPPORTED_SCHEMA_VERSION
        if self.arguments.sbom_schema_version:
            schema_version = SchemaVersion['V{}'.format(str(self.arguments.sbom_schema_version).replace('.', '_'))]

        output: BaseOutput = get_instance(bom=bom, output_format=output_format, schema_version=schema_version)

        if self.arguments.sbom_output_file:
            # Output to a file
            output.output_to_file(filename=self.arguments.sbom_output_file, allow_overwrite=True)
        else:
            # Output to STDOUT
            print(output.output_as_string())

        return 0

    def get_argument_parser_name(self) -> str:
        return 'sbom'

    def get_argument_parser_help(self) -> str:
        return 'generate a CycloneDX software-bill-of-materials (no vulnerabilities)'

    def setup_argument_parser(self, arg_parser: ArgumentParser) -> None:
        arg_parser.add_argument('-i', '--input', action='store', metavar='FILE_PATH',
                                type=FileType('r'), default=(None if sys.stdin.isatty() else sys.stdin),
                                help='Where to get input data from. If a path to a file is not specified directly here,'
                                     'then we will attempt to read data from STDIN. If there is no data on STDIN, we '
                                     'will then fall back to looking for standard files in the current directory that '
                                     'relate to the type of input indicated by the -t flag.', dest='sbom_input_source',
                                required=False)

        arg_parser.add_argument('-t', '--type', '-it', '--input-type',
                                help='how jake should find the packages from which to generate your SBOM.'
                                     'ENV = Read from the current Python Environment; '
                                     'CONDA = Read output from `conda list --explicit`; '
                                     'CONDA_JSON = Read output from `conda list --json`; '
                                     'PIP = read from a requirements.txt; '
                                     'PIPENV = read from Pipfile.lock; '
                                     'POETRY = read from a poetry.lock. '
                                     '(Default = ENV)',
                                metavar='TYPE', choices={'CONDA', 'CONDA_JSON', 'ENV', 'PIP', 'PIPENV', 'POETRY'},
                                default='ENV', dest='sbom_input_type')

        arg_parser.add_argument('-o', '--output-file', help='Specify a file to output the SBOM to',
                                metavar='PATH/TO/FILE',
                                dest='sbom_output_file')
        arg_parser.add_argument('--output-format', help='SBOM output format (default = xml)', choices={'json', 'xml'},
                                default='xml', dest='sbom_output_format')
        arg_parser.add_argument('--schema-version',
                                help=f'CycloneDX schema version to use (default = '
                                     f'{LATEST_SUPPORTED_SCHEMA_VERSION.to_version()})',
                                choices={'1.4', '1.3', '1.2', '1.1', '1.0'},
                                default=f'{LATEST_SUPPORTED_SCHEMA_VERSION.to_version()}',
                                dest='sbom_schema_version')

    def _get_parser(self) -> cyclonedx.parser.BaseParser:
        if self.arguments.sbom_input_type == 'ENV':
            return EnvironmentParser()

        # All other input types require INPUT - let's grab it now if provided via STDIN or supplied FILE
        input_data_fh = self.arguments.sbom_input_source
        if input_data_fh:
            with input_data_fh:
                input_data = input_data_fh.read()
                input_data_fh.close()

            if self.arguments.sbom_input_type == 'CONDA':
                return CondaListExplicitParser(conda_data=input_data)

            if self.arguments.sbom_input_type == 'CONDA_JSON':
                return CondaListJsonParser(conda_data=input_data)

            if self.arguments.sbom_input_type == 'PIP':
                return RequirementsParser(requirements_content=input_data)

            if self.arguments.sbom_input_type == 'PIPENV':
                return PipEnvParser(pipenv_contents=input_data)

            if self.arguments.sbom_input_type == 'POETRY':
                return PoetryParser(poetry_lock_contents=input_data)

        else:
            # No data available on STDIN or the supplied FILE, so we'll try standard filenames in the current directory
            if self.arguments.sbom_input_type == 'PIP':
                return RequirementsFileParser(requirements_file='requirements.txt')

            if self.arguments.sbom_input_type == 'PIPENV':
                return PipEnvFileParser(pipenv_lock_filename='Pipfile.lock')

            if self.arguments.sbom_input_type == 'POETRY':
                return PoetryFileParser(poetry_lock_filename='poetry.lock')

        raise NotImplementedError
