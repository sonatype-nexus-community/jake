# CHANGELOG


## v4.0.0 (2026-05-13)

### Bug Fixes

- _get_max_cvss_score now tracks the highest score across all vulns
  ([`b29908b`](https://github.com/sonatype-nexus-community/jake/commit/b29908bf2ec5619b976cfb4e943b43676f6f1156))

Was reassigning on every loop iteration, so the returned value was the score of the last
  vulnerability rather than the highest. Components with multiple vulnerabilities displayed the
  wrong color and severity label.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Provide Guide authentication feedback using new env variable names
  ([`92e23b5`](https://github.com/sonatype-nexus-community/jake/commit/92e23b508197dfc4e91fb4901ba2681e473b9126))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Remove emoji from Rich output to fix Windows Unicode crash
  ([`6997d9f`](https://github.com/sonatype-nexus-community/jake/commit/6997d9f720e3f03a2ea9308b984871c956f8e4b7))

- Remove all emoji from progress/status strings in oss.py and iq.py - Replace :warning: markup with
  plain text [bright_red](!) indicator - Add Console(highlight=False) in app.py for consistent
  output - Add windows-latest to CI matrix to catch regressions

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Replace pyfiglet with art to fix Python 3.14 startup crash
  ([`26c8311`](https://github.com/sonatype-nexus-community/jake/commit/26c831156b12105252c8188e7b5092f7c4f19d4f))

pyfiglet uses pkg_resources which was removed in Python 3.14. Replace with art library (MIT, no
  pkg_resources dependency).

BREAKING CHANGE: pyfiglet is no longer a dependency

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Address all CI failures from integration branch
  ([`dfe8dc4`](https://github.com/sonatype-nexus-community/jake/commit/dfe8dc4d52106c6c58b479a8c79891d7e7ce6386))

- Rename ScanApi → ThirdPartyAnalysisApi in iq.py (renamed in sonatype-iq-api-client 0.201.0) - Fix
  mypy no-redef: rename whitelist loop variable report → guide_report in oss.py - Fix mypy null
  safety: add `or ''` guard for Optional vuln.reference and vuln.display_name in oss.py - Fix flake8
  E127: reformat _get_max_cvss_score() continuation lines in oss.py - Add type:
  ignore[import-untyped] for art in app.py (missing py.typed marker) - Add type:
  ignore[import-untyped] for packageurl in all five parser files (missing py.typed in lowest deps) -
  Add shell: bash to Run tests step in ci.yml to fix bash syntax on Windows PowerShell runners

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Correct typing and lowest-deps configuration for mypy
  ([`93f7a36`](https://github.com/sonatype-nexus-community/jake/commit/93f7a366712bba3b90a06f39ac6c147d28e07a11))

- requirements.lowest.txt: replace obsolete deps (cyclonedx-bom, ossindex-lib, pyfiglet, polling2,
  requests) with current minimum versions of cyclonedx-python-lib, art, sonatype-guide-api-client,
  sonatype-iq-api-client, rich, tomli - sbom.py: ExternalReference(reference_type=...) → (type=...)
  for all 7 refs — cyclonedx-python-lib 11.x renamed this parameter from reference_type to type -
  iq.py: add null guards for internal_id (str|None) and ticket.status_url (str|None) to satisfy
  ThirdPartyAnalysisApi StrictStr; change source arg from 'jake' to 'cyclonedx' per 0.201.0 API
  requirement - environment.py: annotate seen as set[str] and suppress attr-defined on
  PackageMetadata.get() which is valid at runtime but absent from Protocol stub - poetry.py:
  suppress import-not-found on tomllib which is stdlib on 3.11+ only

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **deps**: Bump rich minimum from 10.10.0 to 13.2.0
  ([`41014e4`](https://github.com/sonatype-nexus-community/jake/commit/41014e48414487544da0d5f02bfeef1ed6839403))

rich <13.2.0 depends on commonmark which transitively pulls in future, exposing CVE-2022-40899. rich
  13.2.0 replaced commonmark with markdown-it-py, eliminating that dependency chain entirely.

Closes #127

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **deps**: Pin urllib3 >= 2.7.0 to remediate CVEs
  ([`b72636c`](https://github.com/sonatype-nexus-community/jake/commit/b72636c6739b19b6ee2e49d2d13c21c32d342971))

urllib3 2.2.3 carries CVE-2025-66418, CVE-2025-66471, CVE-2026-21441 (all CVSS 7.5) and
  CVE-2025-50181 (CVSS 6.1). Adding an explicit floor in pyproject.toml ensures the lock file cannot
  regress to a vulnerable version; both API clients already allow >=2.1.0,<3.0.0 so 2.7.0 is
  compatible.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **iq**: Retry on 404 while waiting for IQ scan results
  ([`1e7c939`](https://github.com/sonatype-nexus-community/jake/commit/1e7c939e755acf6168f256fcdffd93e12e237afd))

IQ Server returns 404 NotFoundException while the scan is still processing. Catch it in the polling
  loop and retry (up to 30 attempts / 300 seconds), mirroring the old polling2-based behaviour.
  Raise RuntimeError if the timeout is exceeded.

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- **iq**: Set Content-Type: application/xml when submitting CycloneDX SBOM
  ([`4d3424b`](https://github.com/sonatype-nexus-community/jake/commit/4d3424b34df4e89ef33e0a37127f35eca603f728))

The sonatype_iq_api_client selects the first accepted content type (application/json) by default.
  Explicitly passing _content_type='application/xml' ensures IQ Server receives the correct header
  and can parse the CycloneDX XML body.

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- **oss**: Show clear auth error message on 401 Unauthorized
  ([`cb86ff7`](https://github.com/sonatype-nexus-community/jake/commit/cb86ff70af362d91ab27fac1f01948521bf24cfc))

Extract Progress block into _perform_scan() so UnauthorizedException can be caught in handle_args()
  after Progress has closed, making the error message visible on the terminal instead of a raw
  traceback.

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- **quality**: Address 4 SonarQube issues on dev/4x/integration
  ([`958eb4b`](https://github.com/sonatype-nexus-community/jake/commit/958eb4b8c390a28a1a28e65bf8410ae1ab779991))

- oss.py: extract 'OSS Index' literal to _OSS_INDEX_SOURCE constant (S1192) - oss.py: remove dead
  else-branch in _print_oss_index_report — the inner `if comp_vulns` check is redundant since the
  outer guard already ensures it; reduces cognitive complexity from 17 to 15 (S3776) -
  parser_selector.py: extract _parser_from_content and _parser_from_file helpers from get_parser;
  reduces cognitive complexity from 19 to 2 (S3776) - requirements.py: replace reluctant quantifier
  .*? with [^\]]* in _PIN_RE for more efficient regex matching (S5857)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ssl**: Add certifi dependency and configure SSL CA bundle for API clients
  ([`ee3995a`](https://github.com/sonatype-nexus-community/jake/commit/ee3995a462491e6d4a6806f440cfdc06cd7a3d59))

Adds certifi as an explicit dependency (>=2024.7.4, patching CVE-2024-39689) and passes
  ssl_ca_cert=certifi.where() to both sonatype_guide_api_client and sonatype_iq_api_client
  Configuration objects. The old ossindex-lib used requests which auto-loaded certifi; the new
  OpenAPI-generated clients use urllib3 directly and require explicit CA bundle configuration to
  work on systems without system CAs accessible to Python.

Also extracts multi-line f-string join expressions in _print_vulnerability to local variables,
  resolving pre-existing flake8 E122 continuation-line warnings.

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

- **typing**: Suppress import-not-found on tomli fallback import
  ([`041ff88`](https://github.com/sonatype-nexus-community/jake/commit/041ff88a73ce53f2ceabc1e0fc79d505d7f5ca6e))

mypy reports import-not-found for tomli on environments where it is not installed (Python 3.11+
  where tomllib is stdlib and tomli is absent). The existing no-redef ignore did not cover this
  error code.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Chores

- Ignore MODERNISATION.md local planning document
  ([`e770375`](https://github.com/sonatype-nexus-community/jake/commit/e770375c29c2f1c3e5b7d0792561c1e4a083cccb))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Update dev tooling for v4.x
  ([`d9e15b7`](https://github.com/sonatype-nexus-community/jake/commit/d9e15b76a1b0daafc87fca668ecc2e59c41c8e6b))

- Rename [tool.poetry.dev-dependencies] to [tool.poetry.group.dev.dependencies] (Poetry 2.x) - Bump
  tox to ^4.0, mypy to ^1.0, flake8 to ^7.0, coverage to ^7.0 - Update tox.ini: allowlist_externals,
  minversion=4.0, mypy --python-version=3.10 - Update CI: POETRY_VERSION to 2.4.1

BREAKING CHANGE: minimum Poetry version is now 2.x

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Correct invocation of jake when integration testing against Sonatype Guide
  ([`fe82fc4`](https://github.com/sonatype-nexus-community/jake/commit/fe82fc4d3fbc3a705394a544ed1b9596ca3cad4e))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Indicate target Python Version to SonarQube
  ([`72f641a`](https://github.com/sonatype-nexus-community/jake/commit/72f641aac35491436b800055cde0ddaecfcaa831))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Update RTD config
  ([`af67a11`](https://github.com/sonatype-nexus-community/jake/commit/af67a116885e4221add18cdb12bf583f9b450d69))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Add Sonatype Guide integration test job
  ([`b72be43`](https://github.com/sonatype-nexus-community/jake/commit/b72be43560760b9c8bf653c4739868d2fc2398c1))

Adds integration-guide job that runs `jake guide -w` against the real Sonatype Guide API after
  build-and-test passes. Uses -w (warn-only) so incidental vulnerabilities in the CI environment do
  not cause failure — the test validates authentication and end-to-end connectivity only.

Secrets OSSI_USERNAME and SONATYPE_GUIDE_TOKEN are injected at step level. The job is skipped on
  fork PRs where repository secrets are unavailable.

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

### Features

- Drop Python 3.8/3.9, target >=3.10,<3.14
  ([`370a56c`](https://github.com/sonatype-nexus-community/jake/commit/370a56ca187a3ce896c1916defa639ac04f13939))

- Constrain python to >=3.10,<3.14 in pyproject.toml - Remove importlib-metadata conditional (stdlib
  in 3.10+) - Update tox envlist to py{313,312,311,310} - Update CI matrix to Python 3.10, 3.11,
  3.12, 3.13 - Remove importlib-metadata from requirements.lowest.txt - Update classifiers to
  reflect supported Python versions

BREAKING CHANGE: Python 3.8 and 3.9 are no longer supported

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Replace hand-rolled IQ client with sonatype-iq-api-client
  ([`8cc6492`](https://github.com/sonatype-nexus-community/jake/commit/8cc6492e788e28130f09837c99530c8a5edfaba9))

- Replace IqServerApi inner class with sonatype-iq-api-client ^0.201.0 - Use
  ApplicationsApi.get_applications() for internal ID lookup - Use ScanApi.scan_components() for BOM
  submission - Use ScanApi.get_scan_status() with polling loop (time.sleep) for results - Remove
  requests and polling2 dependencies - Preserve all existing CLI arguments (-s, -i, -u, -p, -st)

BREAKING CHANGE: hand-rolled IQ REST client replaced by official sonatype-iq-api-client

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Replace ossindex-lib with sonatype-guide-api-client, add guide subcommand
  ([`882fedd`](https://github.com/sonatype-nexus-community/jake/commit/882feddddb8acb73876af66ff40a0d47efa320c5))

- Replace ossindex-lib with sonatype-guide-api-client ^0.1.0 (Apache-2.0) - Rewrite OssCommand to
  use OSSIndexCompatibilityApi with PurlRequestPost - Add -u/--username and --token args (env:
  OSS_INDEX_USERNAME/OSS_INDEX_TOKEN) - Remove --clear-cache (Guide API has no local cache) - Rename
  subcommand from ddt to guide - Add DdtCommand subclass as deprecated alias for ddt subcommand -
  Update app.py to register both guide and ddt subcommands

BREAKING CHANGE: ossindex-lib replaced by sonatype-guide-api-client; ddt is deprecated in favour of
  guide

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Upgrade cyclonedx-bom v3 to cyclonedx-python-lib v11
  ([`0fa0710`](https://github.com/sonatype-nexus-community/jake/commit/0fa07106d7d1324f838c0e029b5bff0231d9983c))

- Replace cyclonedx-bom ^3.0.0 with cyclonedx-python-lib ^11.7.0 - Add tomli ^2.0 backport for
  Python <3.11 (poetry.lock parsing) - Implement jake/_internal/parsers/ replacing removed
  cyclonedx_py parsers: EnvironmentParser, RequirementsParser, PoetryParser, PipenvParser,
  CondaListExplicitParser, CondaListJsonParser - Update parser_selector.py to use new internal
  parsers - Update sbom.py: Bom(components=set(...)), tools.components.add(), make_outputter(),
  SchemaVersion.from_version() - Update oss.py: vulnerabilities on Bom not Component, build vuln_map
  from v.affects - Update iq.py: make_outputter() replacing get_instance() - Move
  OutputFormat/SchemaVersion imports to cyclonedx.schema

BREAKING CHANGE: cyclonedx-bom is replaced by cyclonedx-python-lib v11; CycloneDX schema 1.5 and 1.6
  now supported

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **guide**: Rename env vars to SONATYPE_GUIDE_*, update all docs
  ([`b4a9ff1`](https://github.com/sonatype-nexus-community/jake/commit/b4a9ff10a84ba9bd314c085ae58011c40f5a18d8))

Code: - SONATYPE_GUIDE_USERNAME / SONATYPE_GUIDE_TOKEN are now the primary environment variables for
  `jake guide`; OSS_INDEX_USERNAME / OSS_INDEX_TOKEN are accepted as fallbacks for backward
  compatibility - Update CLI help strings to reference Sonatype Guide, not OSS Index

Docs (README.md, docs/usage.rst, docs/configuration.rst, docs/index.rst): - Replace all OSS Index
  references with Sonatype Guide - Update Python version badge to 3.10+ - Switch CI badge from
  CircleCI to GitHub Actions - Document SONATYPE_GUIDE_* env vars and fallback behaviour - Add
  "Migrating from OSS Index to Sonatype Guide" section covering command rename (ddt → guide), env
  var rename, and breaking changes - Refresh --help output blocks to reflect v4 commands and flags

Signed-off-by: Paul Horton <phorton@sonatype.com>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

### Refactoring

- Extract _build_ratings to reduce Cognitive Complexity in oss.py
  ([`d700989`](https://github.com/sonatype-nexus-community/jake/commit/d70098919c81d2235777c9e33a2919f7babbbd9f))

_build_vulnerability was still at 17 after the prior refactor. Extracting the ratings construction
  into _build_ratings removes the outer if-guard and two redundant ternaries (score/severity were
  guarded by the outer if but repeated the condition), bringing _build_vulnerability to <=15.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Extract helpers to reduce Cognitive Complexity in iq.py and oss.py
  ([`daed157`](https://github.com/sonatype-nexus-community/jake/commit/daed157a228a0c28bec9b4a166cd426c050e8c22))

Fixes two SonarQube S3776 violations introduced on dev/4x/integration: - iq.py: extract
  _poll_scan_result() to bring handle_args from 16 to <=15 - oss.py: extract _build_vulnerability(),
  _apply_whitelist(), and _process_components() to bring _perform_scan from 64 to <=15

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v3.1.0 (2026-05-12)

### Bug Fixes

- Cve-2024-47081 in requests 2.32.3
  ([`803ec4f`](https://github.com/sonatype-nexus-community/jake/commit/803ec4f63e2c117352463065cf69d12a69f38450))

### Chores

- **ci**: Allow brent-spiner to automate releases
  ([`4066b26`](https://github.com/sonatype-nexus-community/jake/commit/4066b261bee24b6cc8cd9c0f68360021d42f1822))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Allow brent-spiner to automate releases
  ([`37fdc17`](https://github.com/sonatype-nexus-community/jake/commit/37fdc1758a7d59c67307043c8169d8b354bea605))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Allow brent-spiner to automate releases
  ([`1eb946c`](https://github.com/sonatype-nexus-community/jake/commit/1eb946cab6a05df116f0cf821d891a686b6361f0))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Allow brent-spiner to automate releases
  ([`8009e8b`](https://github.com/sonatype-nexus-community/jake/commit/8009e8b6829a4e043fe6b285cff702d9e6f9f66e))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **ci**: Update RTD config
  ([`5a614da`](https://github.com/sonatype-nexus-community/jake/commit/5a614dade70c3e2e6b890475e6b662fb5781b554))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **dep**: Use poetry 1.8.3 now
  ([`7766552`](https://github.com/sonatype-nexus-community/jake/commit/77665523db813a415b53a843a649ea0517757bb3))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **deps,ci**: Pinned GH actions in release workflow + upgraded some deps
  ([`a04581b`](https://github.com/sonatype-nexus-community/jake/commit/a04581b10fe2ba7a09125f1a79e620c318d8cf51))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **deps,ci**: Pinned GH actions in release workflow + upgraded some deps
  ([`229471a`](https://github.com/sonatype-nexus-community/jake/commit/229471a7edf2755d94a3c89243c2901529a5e00a))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- **deps,ci**: Pinned GH actions in release workflow + upgraded some deps
  ([`b833bd3`](https://github.com/sonatype-nexus-community/jake/commit/b833bd3f54ebeed84db23dca98d4c66c382c8fca))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Adopt latest Sonatype Community Standards
  ([`23bcb49`](https://github.com/sonatype-nexus-community/jake/commit/23bcb49293f2397282f1b79e3a643c48d0510130))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v3.0.14 (2024-07-18)

### Bug Fixes

- Release script changes
  ([`6efcb5f`](https://github.com/sonatype-nexus-community/jake/commit/6efcb5f0b63a89cab93e3a8ab70644f611de726f))


## v3.0.13 (2024-07-18)

### Bug Fixes

- Cve-2024-5569 in setuptools 70.1.1
  ([`4ceefb8`](https://github.com/sonatype-nexus-community/jake/commit/4ceefb8ff97138b81cc68ac0eccdad26905281e2))


## v3.0.12 (2024-04-18)

### Bug Fixes

- Resolve CVE-2024-3651 in idna-3.6
  ([`218ac49`](https://github.com/sonatype-nexus-community/jake/commit/218ac49ba19001de9a1cedea25d375c6d032d9f0))


## v3.0.11 (2023-12-08)

### Bug Fixes

- Bump toml version one ahead. this one goes to 11
  ([`c3daeb8`](https://github.com/sonatype-nexus-community/jake/commit/c3daeb808931756efc0a295de7eb5238984a4959))


## v3.0.10 (2023-12-08)

### Bug Fixes

- Bump toml version one ahead of latest git tag for first new semantic-release with twine
  credentials
  ([`9a76fe1`](https://github.com/sonatype-nexus-community/jake/commit/9a76fe10a2fadd4995cb5187d56aaa4739c9b913))


## v3.0.9 (2023-12-08)

### Bug Fixes

- Bump toml version one ahead of latest git tag for first new semantic-release
  ([`52d459e`](https://github.com/sonatype-nexus-community/jake/commit/52d459ed2cfb2fe7c78ffe8e35cb0a58210f3343))


## v3.0.8 (2023-12-08)

### Bug Fixes

- Sync versions again manually for first new semantic-release (added git tag)
  ([`d096fc9`](https://github.com/sonatype-nexus-community/jake/commit/d096fc986c6fab471c50d563c40ef3dfb171957e))


## v3.0.3 (2023-12-08)

### Bug Fixes

- Try to sync versions manually for first new semantic-release
  ([`e92ecee`](https://github.com/sonatype-nexus-community/jake/commit/e92ecee264a124c0ca4b20dd5cd08cb189bc9be4))


## v3.0.2 (2023-12-08)

### Bug Fixes

- Kick release harder, update lock file, bump release version, cross fingers.
  ([`474609f`](https://github.com/sonatype-nexus-community/jake/commit/474609f20694b0cdd4297a91d0a7260bd3eee713))

- More verbose semantic-release
  ([`3a87a37`](https://github.com/sonatype-nexus-community/jake/commit/3a87a3715b0e905e0f21670694541561f5ae13c6))

- Resolve CVE-2023-37920 in certifi 2023.5.7
  ([`821380a`](https://github.com/sonatype-nexus-community/jake/commit/821380a4651a57d650d3f6af970ae0ecce9e3608))

- Resolve CVE-2023-43804 in urllib3 2.0.2
  ([#144](https://github.com/sonatype-nexus-community/jake/pull/144),
  [`a39e9d2`](https://github.com/sonatype-nexus-community/jake/commit/a39e9d21f57080edeebdcfecbc3043cb773fe0f4))

- Resolve CVE-2023-45803 in urllib3 2.0.6
  ([`4ffd06b`](https://github.com/sonatype-nexus-community/jake/commit/4ffd06bca7ae896b2a90de57fecb42928e4838fb))

- Small change to trigger release to allow higher rich version
  ([`51cbfd6`](https://github.com/sonatype-nexus-community/jake/commit/51cbfd612cdbe81fa2d0d4e31eca9a31c16a1275))

- Trigger release for vulnerability fixed in dc52c76f
  ([`bcee8a2`](https://github.com/sonatype-nexus-community/jake/commit/bcee8a2dff57b20b1b4bbb43c92c516e52cd3e43))

- Trigger release of 3.0.2
  ([`73ba63f`](https://github.com/sonatype-nexus-community/jake/commit/73ba63f95d75b46c9ad11efe6c5f7bf943419484))

- Update circleci config.yml ([#148](https://github.com/sonatype-nexus-community/jake/pull/148),
  [`1385908`](https://github.com/sonatype-nexus-community/jake/commit/1385908cd978c0fbeb4db3d18fa2aee1f518d67e))

- Verbose semantic-release
  ([`bf975f8`](https://github.com/sonatype-nexus-community/jake/commit/bf975f8eaa84ce7d5e011bcd144f93bb191f8324))

- Verbose semantic-release (bump version)
  ([`b0d102d`](https://github.com/sonatype-nexus-community/jake/commit/b0d102db41af8456029d56840df80957f42017e8))


## v3.0.1 (2023-05-30)

### Bug Fixes

- Cve-2022-23491 in certifi 2022.5.18.1
  ([`d964732`](https://github.com/sonatype-nexus-community/jake/commit/d9647329337d5cb47c02eaa884c613228e8b1bec))

- Cve-2022-23491 in transitive dependency certifi 2022.5.18.1 by upgrading the version in the lock
  file.
  ([`1815487`](https://github.com/sonatype-nexus-community/jake/commit/181548736b0ed0021d78466b2c85413b5b5b6448))

- Handle CWE name suffixed with 'noinfo'
  ([#129](https://github.com/sonatype-nexus-community/jake/pull/129),
  [`a5d0f11`](https://github.com/sonatype-nexus-community/jake/commit/a5d0f11b9e91e0c00ebd4c227115f38e9eab5eb2))

@daviskirk suggestion

Co-authored-by: Davis Kirkendall <1049817+daviskirk@users.noreply.github.com>

- More source file header cleanups
  ([`261a991`](https://github.com/sonatype-nexus-community/jake/commit/261a9914b019a96c895eb1ad4878d3a0482eb4d5))

- Source file header cleanups
  ([`6ebf12d`](https://github.com/sonatype-nexus-community/jake/commit/6ebf12d87e6966876575524853247dd50dc9b49f))

### Documentation

- Fix -f switch in the examples ([#126](https://github.com/sonatype-nexus-community/jake/pull/126),
  [`80ac509`](https://github.com/sonatype-nexus-community/jake/commit/80ac50983c6e7e426d84944b31b3d768c7d3517f))

Co-authored-by: Dan Rollo <danrollo@gmail.com>


## v3.0.0 (2022-12-02)

### Bug Fixes

- Restore running jake on jake
  ([`675b359`](https://github.com/sonatype-nexus-community/jake/commit/675b35927a892755ec5fced019646c043ff3d671))

### Features

- Support for all input formats when running jake ddt or jake iq
  ([#125](https://github.com/sonatype-nexus-community/jake/pull/125),
  [`9a597b5`](https://github.com/sonatype-nexus-community/jake/commit/9a597b59c7f3f042f7188a5cd6a7f6c8c0482f97))

* feat: Support for all input formats when running jake ddt or jake iq

closes #104

BREAKING CHANGE: changed iq -t switch to -st, use common `-f` argument for input file

Co-authored-by: Dan Rollo <danrollo@gmail.com>

### Breaking Changes

- Changed iq -t switch to -st, use common `-f` argument for input file


## v2.1.1 (2022-06-09)

### Bug Fixes

- Removed typo from default value of `--schema-version` argument #117
  ([`e9e4764`](https://github.com/sonatype-nexus-community/jake/commit/e9e47649ab87eacdd0a98d8ee9798615d8913fdf))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Temporarily removed running `jake` against `jake` as this is blocking release - likely due to OSS
  Index updates
  ([`88d390c`](https://github.com/sonatype-nexus-community/jake/commit/88d390c629cc1c2260745dabac3eb744f0448ea3))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v2.1.0 (2022-06-09)

### Chores

- Added unified license headers as per interal Sonatype check
  ([`ccb927b`](https://github.com/sonatype-nexus-community/jake/commit/ccb927b6441002107915cc82461bee80bc7e23c8))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Temporarily removed running `jake` against `jake` as this is blocking release - likely due to OSS
  Index updates
  ([`1da3571`](https://github.com/sonatype-nexus-community/jake/commit/1da3571e1cb2105cba7a65b9f2207ffbd741acca))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Add support for vulnerability whitelist when running `jake ddt` - thanks @daviskirk!
  ([`80e1136`](https://github.com/sonatype-nexus-community/jake/commit/80e113620642a032a767bd064ec317a7f19b7de1))


## v2.0.0 (2022-03-10)


## v1.4.5 (2022-02-15)

### Bug Fixes

- Pin some upstream dependencies to prevent #112
  ([#113](https://github.com/sonatype-nexus-community/jake/pull/113),
  [`8a43e0a`](https://github.com/sonatype-nexus-community/jake/commit/8a43e0af074f797abaddcc0a542b5e08d8a75b36))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Resolve historic oss index caching issues
  ([`dc03aa9`](https://github.com/sonatype-nexus-community/jake/commit/dc03aa923cf2a8c48d0ad9e7e30cb188fb3a5a96))

feat: support for oss index authentication

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Chores

- Bump to latest `cyclonedx-python`
  ([`e437bb4`](https://github.com/sonatype-nexus-community/jake/commit/e437bb41ddbb84d7844f40b213878c67c071cc23))

BREAKING CHANGE: Notion of default schema version has been removed by upstream library and replaced
  with latest supported schema version

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Bumped dependencies ([#107](https://github.com/sonatype-nexus-community/jake/pull/107),
  [`2ee98fe`](https://github.com/sonatype-nexus-community/jake/commit/2ee98fea6453003b4581dbd02127009ae5b91a82))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Support for Python 3.10 ([#110](https://github.com/sonatype-nexus-community/jake/pull/110),
  [`671c8c4`](https://github.com/sonatype-nexus-community/jake/commit/671c8c4bb682b4b944568198ecf381818d49f3ac))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Typing as per PEP-561 and other refactors
  ([#114](https://github.com/sonatype-nexus-community/jake/pull/114),
  [`a0ab7ee`](https://github.com/sonatype-nexus-community/jake/commit/a0ab7eecac96ea9dd1324117651556493247eb98))

* feat: typing of `jake` WIP

Signed-off-by: Paul Horton <phorton@sonatype.com>

* port of fix for #112

* resolved a bunch of typing issues

* ci: fixed parameter references

* ci: fixed mypy

* fix: updated `ossindex-lib` to latest RC which now appears to properly resolve caching issues #100

* defined lowest dependencies and aligned

* WIP: JSON output updated to use JSON serialisation - All tests passing locally

### Breaking Changes

- Notion of default schema version has been removed by upstream library and replaced with latest
  supported schema version


## v1.4.4 (2022-02-08)

### Bug Fixes

- Cwes are `int` and needed to be stringified
  ([#102](https://github.com/sonatype-nexus-community/jake/pull/102),
  [`3e15cb1`](https://github.com/sonatype-nexus-community/jake/commit/3e15cb16c037d8bb09eb5c38dbd239dd345f09cc))

fix: Vulnerability rating score now formatted to 1 decimal place

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.4.3 (2022-02-03)

### Bug Fixes

- Cwes not passed as ints to CDX model
  ([#97](https://github.com/sonatype-nexus-community/jake/pull/97),
  [`6ec49a6`](https://github.com/sonatype-nexus-community/jake/commit/6ec49a6a7d2b22b2535346409ee49fc3cd5f2c8b))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.4.2 (2022-01-31)

### Bug Fixes

- Corrected data placement for Vulnerabilities returned from OSS Index when generating an SBOM
  ([#94](https://github.com/sonatype-nexus-community/jake/pull/94),
  [`eb12286`](https://github.com/sonatype-nexus-community/jake/commit/eb1228602c63784da751749cce14ee9fec9f3d1f))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.4.1 (2022-01-24)

### Bug Fixes

- `bom-ref` will always now be populated for Component and Vulnerability - bump of
  `cyclonedx-python-lib` solves this
  ([#92](https://github.com/sonatype-nexus-community/jake/pull/92),
  [`df2aad2`](https://github.com/sonatype-nexus-community/jake/commit/df2aad2fa23548e98d2857e2f038e4850067f9b6))

fix: complete `affects` for vulnerabilities received from OSS Index

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.4.0 (2022-01-13)

### Features

- Support CycloneDX 1.4 ([#87](https://github.com/sonatype-nexus-community/jake/pull/87),
  [`20c62fc`](https://github.com/sonatype-nexus-community/jake/commit/20c62fcb70d1245e5c31df56ad3d71bc9e7fe0d0))

* fix: unified how current version of `jake` is collected

Signed-off-by: Paul Horton <phorton@sonatype.com>

* feat: adopted latest RC for CycloneDX libraries to enable 1.4 support

* fixes

* chore: bumped to released versions of CyloneDX libraries`


## v1.3.0 (2022-01-11)

### Features

- **pre-commit**: Add pre-commit hooks
  ([#85](https://github.com/sonatype-nexus-community/jake/pull/85),
  [`45f108e`](https://github.com/sonatype-nexus-community/jake/commit/45f108e018925f932768f29855b19342fcec2ac1))


## v1.2.3 (2021-12-22)

### Bug Fixes

- Resolved regression when running `jake ddt` where return code != 0 when vulnerabilities discovered
  ([`8a10e70`](https://github.com/sonatype-nexus-community/jake/commit/8a10e700cea51b649ef7f2271a44e42109264e9a))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.2.2 (2021-12-15)

### Bug Fixes

- Removed a number of direct dependencies that are now transitives, or no longer required
  ([`bcb0a3d`](https://github.com/sonatype-nexus-community/jake/commit/bcb0a3d222c23f88e92fc74c37fd2864e236d8d5))


## v1.2.1 (2021-12-15)

### Bug Fixes

- Bumped dependencies to resolve wheel-only installation
  ([`4ac980d`](https://github.com/sonatype-nexus-community/jake/commit/4ac980d0d7696128e03f982de2dabdfaf7009e03))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Disabled GitHub Workflows as per #76
  ([`08fd4a4`](https://github.com/sonatype-nexus-community/jake/commit/08fd4a47c0b3d9b8fea7217e894dda61294ac9a7))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.2.0 (2021-12-13)

### Bug Fixes

- Removed f-strings as not required
  ([`b5b271e`](https://github.com/sonatype-nexus-community/jake/commit/b5b271ed78b97101e9fca2e31b2789540bf66fd4))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Chores

- Resolved merge in from master
  ([`3ba93e3`](https://github.com/sonatype-nexus-community/jake/commit/3ba93e3d58aa495d81b5c19271f48790b4608d84))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Replaced `yaspin`, `termcolor` and `terminaltable` with `rich` - see #72, #73, #77
  ([`8534ad9`](https://github.com/sonatype-nexus-community/jake/commit/8534ad92acf6b70407492e55ec68ede3190a393b))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.1.5 (2021-12-09)

### Bug Fixes

- Bump required version of cyclonedx-python-lib to help lax transitive dependencies
  ([`f53407f`](https://github.com/sonatype-nexus-community/jake/commit/f53407fb72625420f015db59bb801cc12ab290cf))

- Bump required version of cyclonedx-python-lib to help lax transitive dependencies
  ([`34e501d`](https://github.com/sonatype-nexus-community/jake/commit/34e501d062da5607f86879e136d1f988de6dd872))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Removed `terminaltables` and replaced with `rich`s table implementation
  ([`416b03c`](https://github.com/sonatype-nexus-community/jake/commit/416b03c0c844a28512143826453ad956e98abd7c))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Removed `yaspin` and replaced with `rich`
  ([`76c4a54`](https://github.com/sonatype-nexus-community/jake/commit/76c4a5451e04c28612ab3c034bbd4a84fa413c94))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.1.4 (2021-12-07)

### Bug Fixes

- Ensure dependencies can be installed from binary packages #72
  ([`9e30ca8`](https://github.com/sonatype-nexus-community/jake/commit/9e30ca8d11bc6ee578749686ff3af30b1c805b10))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Update CI to only install binary packages
  ([`63acf2c`](https://github.com/sonatype-nexus-community/jake/commit/63acf2c20c143c958a1457756d7002a29491f9f3))

Signed-off-by: Paul Horton <phorton@sonatype.com>


## v1.1.3 (2021-11-10)

### Bug Fixes

- Return exit code up the call stack
  ([`12caad2`](https://github.com/sonatype-nexus-community/jake/commit/12caad22e2c5bca95d4f2a4bafae5b95b4a7fd2a))


## v1.1.2 (2021-11-10)

### Bug Fixes

- Restore "stage" parameter for iq command, for realsies
  ([`f1d8c64`](https://github.com/sonatype-nexus-community/jake/commit/f1d8c64853c707ccd07dcceb5bd04bffbd4078db))


## v1.1.1 (2021-11-09)

### Bug Fixes

- Restore "stage" parameter for iq command
  ([`01a41da`](https://github.com/sonatype-nexus-community/jake/commit/01a41dae1ca8f13d7f3837f695daa25792f9e834))


## v1.1.0 (2021-10-22)

### Features

- Add support for conda #66
  ([`a3495cb`](https://github.com/sonatype-nexus-community/jake/commit/a3495cb55fe835181ae57a1a48b9ff8cbe7b7415))


## v1.0.1 (2021-10-20)

### Bug Fixes

- Update to support returning non-zero exit code when issues found (will return 1)
  ([`7667bac`](https://github.com/sonatype-nexus-community/jake/commit/7667bacb171803f7963bec12240520985103d06c))


## v1.0.0 (2021-10-18)

### Bug Fixes

- Additional whitespace removed
  ([`709f7a2`](https://github.com/sonatype-nexus-community/jake/commit/709f7a2aa752668daba99c04b36ad9b8a6d271f2))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Runtime tweaks to make it more robust
  ([`13c9028`](https://github.com/sonatype-nexus-community/jake/commit/13c902838008377e11e4c47ed619401776b8f782))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Typos noted as updating documentation
  ([`0d65116`](https://github.com/sonatype-nexus-community/jake/commit/0d65116a17757b1ccf4c73bc463ee677eef0d5ff))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Build System

- Now using officially published version of ossindex-lib
  ([`5241427`](https://github.com/sonatype-nexus-community/jake/commit/5241427ffa542f650c776de3d727759b4c0a1916))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Continuous Integration

- Aligned to previous CircleCI context
  ([`f8e9833`](https://github.com/sonatype-nexus-community/jake/commit/f8e98337ee61134681490d2318d05ec4172d4ea1))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Alternative attempt to set Git Author
  ([`5773199`](https://github.com/sonatype-nexus-community/jake/commit/577319906c17ce202d2eb415714f091438c97325))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Alternative attempt to set Git Author
  ([`bdc0931`](https://github.com/sonatype-nexus-community/jake/commit/bdc093171a4aed22489b57cdc0a8e0b4b62f8f1a))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Attempt to get semantic-release running on CircleCI
  ([`1e610e1`](https://github.com/sonatype-nexus-community/jake/commit/1e610e1795e29102e7b5816124d8cd215d58f49a))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Defined commit_author for semantic-release
  ([`d0dcf15`](https://github.com/sonatype-nexus-community/jake/commit/d0dcf15d8bc9c21178fb7a739531a79f25fdccd2))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Disable Release Job on CircleCI and move back to GitHub Action
  ([`6ebb6df`](https://github.com/sonatype-nexus-community/jake/commit/6ebb6df80d8813fb92456b9ca500a97f1707bdf6))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Disabled GitHub Action for deployment
  ([`daebf39`](https://github.com/sonatype-nexus-community/jake/commit/daebf399b76db27c6d5207ac8ce233878f626b0e))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Fix cache key for release CircleCI job
  ([`a730e9e`](https://github.com/sonatype-nexus-community/jake/commit/a730e9e27ba52b1fe27263161296457d57f8b995))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Further work on CircleCI config
  ([`bc42408`](https://github.com/sonatype-nexus-community/jake/commit/bc424085efc64f9a39a2ed3ee50ba76376f7f5be))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Move from CircleCI to GitHub actions
  ([`6d73b10`](https://github.com/sonatype-nexus-community/jake/commit/6d73b10ef6bd6ccea90f9e1f0e34348b09dfe59f))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Re-introduce CircleCI with updated implementation
  ([`59c6b62`](https://github.com/sonatype-nexus-community/jake/commit/59c6b62030e37ac74ce997756339833acac0ed1e))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Remove --noop from semantic-release
  ([`e41a7a2`](https://github.com/sonatype-nexus-community/jake/commit/e41a7a2825b8c6101805c2838709384d86a20a5a))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Update CircleCI release to run on every commit to main
  ([`a5fc8b8`](https://github.com/sonatype-nexus-community/jake/commit/a5fc8b899142bc7e8818e07328616c6413553a11))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Use CircleCI context for PYPI_TOKEN and re-introduced SSH key to attempt to resolve GitHub
  connectivity during release
  ([`26621ac`](https://github.com/sonatype-nexus-community/jake/commit/26621ac212cc1b72e76c58f78ebeb58452c52141))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Features

- Jake's OSS calls now utilising ossindex-lib and cyclonedx-python-lib
  ([`ec83583`](https://github.com/sonatype-nexus-community/jake/commit/ec83583520aa5ff8180b215b55846ed7a6fd487c))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Sonatype Nexus IQ Lifecycle analysis is now migrated to using cyclonedx-python-lib
  ([`214d182`](https://github.com/sonatype-nexus-community/jake/commit/214d1821fa94ff895a2bfa4eac0f6961df093f46))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Support Poetry for gleaning packages within the current environment to generate an SBOM
  ([`b9a1e5d`](https://github.com/sonatype-nexus-community/jake/commit/b9a1e5d2f38963a033d102399827c5c4dfe786da))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Refactoring

- Re-write to consume new cyclonedx-python-lib
  ([`e11cb20`](https://github.com/sonatype-nexus-community/jake/commit/e11cb208c215169d6ce24fa8898a5aa2402d8791))

BREAKING CHANGE: `jake` has been re-written in large part to consume two new external libraries: -
  `cyclonedx-python-lib` which gives `jake` ability to more easily consume your depenedencies in a
  variety of manners (environment, Pipfile.lock, poetry.lock, requirements.txt) and support output
  in both JSON and XML at different schema versions - `ossindex-lib`: most of the functionallity for
  talking to OSS Index that was in `jake` has been externalised to this library to allow others to
  consume it

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Removed unused files
  ([`82492b3`](https://github.com/sonatype-nexus-community/jake/commit/82492b35f20b4da74243890f59a603adb552e7eb))

Signed-off-by: Paul Horton <phorton@sonatype.com>

- Removing old Jake code superseded by cyclonedx-python-lib and ossindex-lib
  ([`d8941f5`](https://github.com/sonatype-nexus-community/jake/commit/d8941f57575ab2cb0d2e334ce546cf11af8ab63a))

Signed-off-by: Paul Horton <phorton@sonatype.com>

### Breaking Changes

- `jake` has been re-written in large part to consume two new external libraries:


## v0.2.77 (2021-07-06)

### Bug Fixes

- Cve-2021-33503 in urllib3 == 1.26.4
  ([#62](https://github.com/sonatype-nexus-community/jake/pull/62),
  [`9dfbb1c`](https://github.com/sonatype-nexus-community/jake/commit/9dfbb1c18831a1456803299e2f98a95ba95ea2b8))


## v0.2.76 (2021-06-29)

### Bug Fixes

- "modulenotfounderror: No module named 'typing_extensions'", occurring in
  'python3.7/site-packages/tinydb/queries.py", line 28' on Jenkins CI
  ([#61](https://github.com/sonatype-nexus-community/jake/pull/61),
  [`a747750`](https://github.com/sonatype-nexus-community/jake/commit/a7477505a0e6d1b198461a75ef8d755cc37dfe12))


## v0.2.75 (2021-05-25)


## v0.2.74 (2021-05-25)


## v0.2.73 (2021-05-25)


## v0.2.72 (2021-05-13)

### Bug Fixes

- Inline targets help changes ([#58](https://github.com/sonatype-nexus-community/jake/pull/58),
  [`c146a7d`](https://github.com/sonatype-nexus-community/jake/commit/c146a7d87e0859040b01278de8a2d09eb9b8b1cb))

* added example to readme of site-packages target list generation in-line to the flag argument

* added site-packages one-liner to -t help description and updated readme to include an example
  invocation


## v0.2.71 (2021-05-13)

### Bug Fixes

- #49 allow newer version of dependencies
  ([#57](https://github.com/sonatype-nexus-community/jake/pull/57),
  [`15553d4`](https://github.com/sonatype-nexus-community/jake/commit/15553d43932feca9978931734cf70c655158417d))

* fix: #49 allow newer version of dependencies, click lib had issues. fix db call. * lockdown
  development dependency versions


## v0.2.70 (2021-04-07)

### Bug Fixes

- Cve-2020-14343 in PyYAML==5.3.1
  ([`11dc3c9`](https://github.com/sonatype-nexus-community/jake/commit/11dc3c90a2df876e2cda02be33a38c5f2a0c3fc4))


## v0.2.69 (2021-03-25)

### Bug Fixes

- Cve-2021-28957 in lxml==4.6.2
  ([`6d4373c`](https://github.com/sonatype-nexus-community/jake/commit/6d4373cd8fe320a17d3f8ca95208a0d5b38888ee))


## v0.2.68 (2021-03-23)


## v0.2.67 (2021-03-18)


## v0.2.66 (2021-02-11)


## v0.2.65 (2021-01-27)


## v0.2.64 (2020-12-17)


## v0.2.63 (2020-12-17)


## v0.2.62 (2020-12-17)


## v0.2.61 (2020-12-17)


## v0.2.60 (2020-12-16)


## v0.2.59 (2020-12-09)

### Bug Fixes

- Resolve vulnerability: CVE-2020-27783 in lxml
  ([`7526728`](https://github.com/sonatype-nexus-community/jake/commit/7526728623e102fb75fad30eb82be8824abbdf39))


## v0.2.58 (2020-12-07)


## v0.2.57 (2020-11-12)


## v0.2.56 (2020-11-12)


## v0.2.55 (2020-11-12)


## v0.2.54 (2020-11-12)


## v0.2.53 (2020-11-12)


## v0.2.52 (2020-11-12)


## v0.2.51 (2020-11-11)


## v0.2.50 (2020-11-09)


## v0.2.49 (2020-09-25)


## v0.2.48 (2020-09-22)


## v0.2.47 (2020-09-22)


## v0.2.46 (2020-09-22)


## v0.2.45 (2020-09-21)


## v0.2.44 (2020-09-21)


## v0.2.43 (2020-09-21)


## v0.2.42 (2020-09-21)


## v0.2.41 (2020-09-21)


## v0.2.40 (2020-09-21)


## v0.2.39 (2020-09-21)


## v0.2.38 (2020-09-21)


## v0.2.37 (2020-09-21)


## v0.2.36 (2020-09-21)


## v0.2.35 (2020-09-21)


## v0.2.34 (2020-09-21)


## v0.2.33 (2020-09-21)


## v0.2.32 (2020-09-21)


## v0.2.31 (2020-09-21)


## v0.2.30 (2020-09-21)


## v0.2.29 (2020-09-21)


## v0.2.28 (2020-09-18)


## v0.2.27 (2020-09-11)


## v0.2.26 (2020-09-10)


## v0.2.25 (2020-09-03)


## v0.2.24 (2020-06-05)


## v0.2.23 (2020-05-29)


## v0.2.22 (2020-05-29)


## v0.2.21 (2020-05-29)


## v0.2.20 (2020-05-29)


## v0.2.19 (2020-05-29)


## v0.2.18 (2020-05-29)


## v0.2.17 (2020-05-29)


## v0.2.16 (2020-05-29)


## v0.2.15 (2020-05-28)


## v0.2.14 (2020-05-28)


## v0.2.13 (2020-05-28)


## v0.2.12 (2020-05-28)


## v0.2.11 (2020-05-28)


## v0.2.10 (2020-05-28)


## v0.2.9 (2020-05-28)


## v0.2.8 (2020-05-28)


## v0.2.7 (2020-05-28)


## v0.2.6 (2020-05-28)


## v0.2.5 (2020-05-28)


## v0.2.4 (2020-05-28)


## v0.2.3 (2020-05-21)


## v0.2.2 (2020-05-20)


## v0.2.1 (2020-05-12)


## v0.2.0 (2020-05-12)


## v0.1.7 (2020-05-01)


## v0.1.6 (2020-04-30)


## v0.1.5 (2020-04-30)


## v0.1.4 (2020-04-24)


## v0.1.3 (2020-04-24)


## v0.1.2 (2020-04-23)


## v0.1.1 (2020-04-23)


## v0.1.0 (2020-04-23)


## v0.0.21 (2020-01-11)


## v0.0.20 (2020-01-08)


## v0.0.19 (2020-01-08)


## v0.0.18 (2020-01-06)


## v0.0.17 (2020-01-03)


## v0.0.16 (2019-11-13)


## v0.0.15 (2019-11-11)


## v0.0.14 (2019-11-08)


## v0.0.13 (2019-11-06)


## v0.0.12 (2019-11-06)


## v0.0.10 (2019-11-06)


## v0.0.9 (2019-11-06)


## v0.0.8 (2019-11-06)


## v0.0.7 (2019-11-06)


## v0.0.6 (2019-11-06)


## v0.0.5 (2019-11-05)


## v0.0.4 (2019-11-05)


## v0.0.3 (2019-11-05)


## v0.0.2 (2019-11-05)


## v0.0.1 (2019-11-05)


## v0.0.0 (2019-11-05)
