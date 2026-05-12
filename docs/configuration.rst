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

Configuration
====================================================

Sonatype Guide
----------------------------------------------------

``jake guide`` queries `Sonatype Guide`_ to check your Python dependencies for known vulnerabilities.
Authentication is required — sign up for a free account at `guide.sonatype.com`_ and generate an API token
from your profile settings.

Supply credentials via environment variables (recommended for CI/CD):

.. code-block::

    export SONATYPE_GUIDE_USERNAME=your@email.com
    export SONATYPE_GUIDE_TOKEN=your-api-token
    jake guide

Or pass them directly on the command line:

.. code-block::

    jake guide -u your@email.com --token your-api-token

**Fallback support for OSS Index variables**

If you are migrating from jake v3, the legacy ``OSS_INDEX_USERNAME`` and ``OSS_INDEX_TOKEN`` environment
variables are still accepted as fallbacks when the new ``SONATYPE_GUIDE_*`` variables are not set.

.. list-table::
   :header-rows: 1

   * - Primary (v4)
     - Fallback (v3 legacy)
   * - ``SONATYPE_GUIDE_USERNAME``
     - ``OSS_INDEX_USERNAME``
   * - ``SONATYPE_GUIDE_TOKEN``
     - ``OSS_INDEX_TOKEN``

Sonatype Nexus Lifecycle
----------------------------------------------------

``jake iq`` submits a CycloneDX SBOM to a `Sonatype Lifecycle`_ server for policy evaluation.
All connection parameters are supplied on the command line:

.. code-block::

    jake iq -s https://my-nexus-lifecycle -i APP_ID -u USERNAME -p PASSWORD

See ``jake iq --help`` for the full list of options.


.. _Sonatype Guide: https://guide.sonatype.com
.. _guide.sonatype.com: https://guide.sonatype.com
.. _Sonatype Lifecycle: https://www.sonatype.com/products/open-source-security-dependency-management
