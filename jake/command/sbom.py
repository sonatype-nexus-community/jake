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

from argparse import ArgumentParser

from cyclonedx.model import ExternalReference
from cyclonedx.model import ExternalReferenceType
from cyclonedx.model import XsUri
from cyclonedx.model.bom import Bom
from cyclonedx.model.component import Component, ComponentType
from cyclonedx.output import BaseOutput, make_outputter
from cyclonedx.schema import OutputFormat, SchemaVersion

from . import BaseCommand
from . import jake_version
from . import parser_selector

_LATEST_SCHEMA_VERSION = max(SchemaVersion)

ThisTool = Component(
    type=ComponentType.APPLICATION,
    name='jake',
    version=jake_version or 'UNKNOWN',
    external_references=[
        ExternalReference(
            type=ExternalReferenceType.BUILD_SYSTEM,
            url=XsUri('https://app.circleci.com/pipelines/github/sonatype-nexus-community/jake')
        ),
        ExternalReference(
            type=ExternalReferenceType.DISTRIBUTION,
            url=XsUri('https://pypi.org/project/jake/')
        ),
        ExternalReference(
            type=ExternalReferenceType.ISSUE_TRACKER,
            url=XsUri('https://github.com/sonatype-nexus-community/jake/issues')
        ),
        ExternalReference(
            type=ExternalReferenceType.LICENSE,
            url=XsUri('https://github.com/sonatype-nexus-community/jake/blob/main/LICENSE')
        ),
        ExternalReference(
            type=ExternalReferenceType.RELEASE_NOTES,
            url=XsUri('https://github.com/sonatype-nexus-community/jake/blob/main/CHANGELOG.md')
        ),
        ExternalReference(
            type=ExternalReferenceType.VCS,
            url=XsUri('https://github.com/sonatype-nexus-community/jake')
        ),
        ExternalReference(
            type=ExternalReferenceType.WEBSITE,
            url=XsUri('https://www.sonatype.com/products/free-developer-tools')
        ),
    ]
)


class SbomCommand(BaseCommand):

    def handle_args(self) -> int:
        bom = Bom(components=set(
            parser_selector.get_parser(self.arguments.sbom_input_type, self.arguments.sbom_input_source)
            .get_components()
        ))
        bom.metadata.tools.components.add(ThisTool)

        output_format = OutputFormat.XML
        if self.arguments.sbom_output_format == 'json':
            output_format = OutputFormat.JSON

        schema_version = _LATEST_SCHEMA_VERSION
        if self.arguments.sbom_schema_version:
            schema_version = SchemaVersion.from_version(str(self.arguments.sbom_schema_version))

        output: BaseOutput = make_outputter(bom, output_format, schema_version)

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
        parser_selector.add_parser_selector_arguments(arg_parser)
        arg_parser.add_argument('-o', '--output-file', help='Specify a file to output the SBOM to',
                                metavar='PATH/TO/FILE',
                                dest='sbom_output_file')
        arg_parser.add_argument('--output-format', help='SBOM output format (default = xml)', choices={'json', 'xml'},
                                default='xml', dest='sbom_output_format')
        arg_parser.add_argument('--schema-version',
                                help=f'CycloneDX schema version to use (default = '
                                     f'{_LATEST_SCHEMA_VERSION.to_version()})',
                                choices={'1.6', '1.5', '1.4', '1.3', '1.2', '1.1', '1.0'},
                                default=f'{_LATEST_SCHEMA_VERSION.to_version()}',
                                dest='sbom_schema_version')
