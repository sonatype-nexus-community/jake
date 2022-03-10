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

Starting with ``jake`` ``2.0.0``, the following configuration can be used.

OSS Index
----------------------------------------------------

Caching of OSS Index responses is performed as `OSS Index`_ has rate limiting in place. One mechanism you can employ to
increase the API limits is to `register for free`_ and supply your OSS Index credentials to ``jake``.

Once you are registered, you can create a YAML config file locally at ``$HOME/.oss-index.config`` with contents as
follows:

.. code-block::

   usernanme: my-oss-index-username
   password: my-oss-index-password



.. _OSS Index: https://ossindex.sonatype.org/
.. _register for free: https://ossindex.sonatype.org/user/register