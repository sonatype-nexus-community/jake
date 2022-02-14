.. #
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

Jake's Documentation
====================================================

``jake`` is a tool to check for your Python environments and applications that can:

1. produce CycloneDX software bill-of-materials
2. report on known vulnerabilities

``jake`` is powered by `Sonatype OSS Index`_ and can also be used with `Sonatype's Nexus IQ Server`_.

Internally, ``jake`` utilises libraries from `CycloneDX`_ when producing Software Bill of Materials.

CycloneDX is a lightweight BOM specification that is easily created, human-readable, and simple to parse.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   usage
   support
   changelog


.. _Sonatype OSS Index: https://ossindex.sonatype.org/
.. _Sonatype's Nexus IQ Server: https://www.sonatype.com/products/open-source-security-dependency-management
.. _CycloneDX: https://cyclonedx.org/tool-center/