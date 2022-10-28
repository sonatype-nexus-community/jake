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
from argparse import ArgumentParser

from cyclonedx.model import ExternalReference
from cyclonedx.model import ExternalReferenceType
from cyclonedx.model import Tool
from cyclonedx.model import XsUri
from cyclonedx.model.bom import Bom
from cyclonedx.output import BaseOutput
from cyclonedx.output import LATEST_SUPPORTED_SCHEMA_VERSION
from cyclonedx.output import OutputFormat
from cyclonedx.output import SchemaVersion
from cyclonedx.output import get_instance

from . import BaseCommand
from . import jake_version
from . import parser_selector

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
        bom = Bom.from_parser(
            parser=parser_selector.get_parser(self.arguments.sbom_input_type, self.arguments.sbom_input_source)
        )
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
        parser_selector.add_parser_selector_arguments(arg_parser)
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
