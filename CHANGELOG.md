# CHANGELOG



## v3.0.8 (2023-12-08)

### Fix

* fix: sync versions again manually for first new semantic-release (added git tag) ([`d096fc9`](https://github.com/sonatype-nexus-community/jake/commit/d096fc986c6fab471c50d563c40ef3dfb171957e))


## v3.0.7 (2023-12-08)

### Fix

* fix: try to sync versions manually for first new semantic-release ([`e92ecee`](https://github.com/sonatype-nexus-community/jake/commit/e92ecee264a124c0ca4b20dd5cd08cb189bc9be4))


## v3.0.2 (2023-12-08)

### Fix

* fix: Update circleci config.yml (#148) ([`1385908`](https://github.com/sonatype-nexus-community/jake/commit/1385908cd978c0fbeb4db3d18fa2aee1f518d67e))

* fix: more verbose semantic-release ([`3a87a37`](https://github.com/sonatype-nexus-community/jake/commit/3a87a3715b0e905e0f21670694541561f5ae13c6))

* fix: verbose semantic-release (bump version) ([`b0d102d`](https://github.com/sonatype-nexus-community/jake/commit/b0d102db41af8456029d56840df80957f42017e8))

* fix: verbose semantic-release ([`bf975f8`](https://github.com/sonatype-nexus-community/jake/commit/bf975f8eaa84ce7d5e011bcd144f93bb191f8324))

* fix: kick release harder, update lock file, bump release version, cross fingers. ([`474609f`](https://github.com/sonatype-nexus-community/jake/commit/474609f20694b0cdd4297a91d0a7260bd3eee713))

* fix: trigger release of 3.0.2 ([`73ba63f`](https://github.com/sonatype-nexus-community/jake/commit/73ba63f95d75b46c9ad11efe6c5f7bf943419484))

* fix: small change to trigger release to allow higher rich version ([`51cbfd6`](https://github.com/sonatype-nexus-community/jake/commit/51cbfd612cdbe81fa2d0d4e31eca9a31c16a1275))

* fix: resolve CVE-2023-45803 in urllib3 2.0.6 ([`4ffd06b`](https://github.com/sonatype-nexus-community/jake/commit/4ffd06bca7ae896b2a90de57fecb42928e4838fb))

* fix: resolve CVE-2023-43804 in urllib3 2.0.2 (#144) ([`a39e9d2`](https://github.com/sonatype-nexus-community/jake/commit/a39e9d21f57080edeebdcfecbc3043cb773fe0f4))

* fix: trigger release for vulnerability fixed in dc52c76f ([`bcee8a2`](https://github.com/sonatype-nexus-community/jake/commit/bcee8a2dff57b20b1b4bbb43c92c516e52cd3e43))

* fix: resolve CVE-2023-37920 in certifi 2023.5.7 ([`821380a`](https://github.com/sonatype-nexus-community/jake/commit/821380a4651a57d650d3f6af970ae0ecce9e3608))

### Unknown

* Update pyproject.toml - allow higher rich version (#147)

* Update pyproject.toml

* Update jake-whitelist.json ([`a70bb1c`](https://github.com/sonatype-nexus-community/jake/commit/a70bb1ce12bee6ed3e3bcc387902d822873b7271))

* update python version badge to 3.7+ ([`9b4e6cb`](https://github.com/sonatype-nexus-community/jake/commit/9b4e6cbb78d3cd0d090ad1b996b63fa2adafec7c))

* remove trigger readme.md change ([`616bf71`](https://github.com/sonatype-nexus-community/jake/commit/616bf71cd507b04a84c9692e9fb5b25747ecd35a))

* Fix cython_sources build error (#142)

* upgrade lowest to ossindex-lib 1.1.1, which fixes cython_sources error when building PyYAML 5.4.1 ([`47371c8`](https://github.com/sonatype-nexus-community/jake/commit/47371c8c98deeb657f826250c2105897c57c9b9e))

* temporary revert of resolve CVE-2023-37920 ([`dc52c76`](https://github.com/sonatype-nexus-community/jake/commit/dc52c76f3ad0bbbd46a92129ad397e9a24ba7c73))

* resolve CVE-2023-37920 ([`9050ebc`](https://github.com/sonatype-nexus-community/jake/commit/9050ebcd4c67d1dae95bdd01959067400a1e780a))


## v3.0.1 (2023-05-30)

### Documentation

* docs: fix -f switch in the examples (#126)

Co-authored-by: Dan Rollo &lt;danrollo@gmail.com&gt; ([`80ac509`](https://github.com/sonatype-nexus-community/jake/commit/80ac50983c6e7e426d84944b31b3d768c7d3517f))

### Fix

* fix: handle CWE name suffixed with &#39;noinfo&#39; (#129)

@daviskirk suggestion

Co-authored-by: Davis Kirkendall &lt;1049817+daviskirk@users.noreply.github.com&gt; ([`a5d0f11`](https://github.com/sonatype-nexus-community/jake/commit/a5d0f11b9e91e0c00ebd4c227115f38e9eab5eb2))

* fix: CVE-2022-23491 in transitive dependency certifi 2022.5.18.1 by upgrading the version in the lock file. ([`1815487`](https://github.com/sonatype-nexus-community/jake/commit/181548736b0ed0021d78466b2c85413b5b5b6448))

* fix: CVE-2022-23491 in certifi 2022.5.18.1 ([`d964732`](https://github.com/sonatype-nexus-community/jake/commit/d9647329337d5cb47c02eaa884c613228e8b1bec))

* fix: more source file header cleanups ([`261a991`](https://github.com/sonatype-nexus-community/jake/commit/261a9914b019a96c895eb1ad4878d3a0482eb4d5))

* fix: source file header cleanups ([`6ebf12d`](https://github.com/sonatype-nexus-community/jake/commit/6ebf12d87e6966876575524853247dd50dc9b49f))

### Unknown

* Merge pull request #141 from sonatype-nexus-community/py7_ci

Drop python 3.6 support, CI fixes ([`4b5b4b7`](https://github.com/sonatype-nexus-community/jake/commit/4b5b4b7901d4c332aa36345650a3f0d5f8403621))

* resolve CVE-2022-42969 ([`4e08241`](https://github.com/sonatype-nexus-community/jake/commit/4e08241ec2ce4607ea8b4def85c646105e0cb370))

* revert ignore ([`2c8f04d`](https://github.com/sonatype-nexus-community/jake/commit/2c8f04d3125d3f28d9dcff834d29d4b3013e4cc2))

* newest poetry ([`eedd043`](https://github.com/sonatype-nexus-community/jake/commit/eedd0432de871652916bd89cd6a2e21970bfa9a0))

* bump min requests ([`2c30049`](https://github.com/sonatype-nexus-community/jake/commit/2c3004937053013363d8ee05a716a2f9c1f5023b))

* bump min importlib-metadata ([`7421a73`](https://github.com/sonatype-nexus-community/jake/commit/7421a73bbce6514af22e0909df3880796d1b6b6c))

* flail3 tox ([`1d2d8c6`](https://github.com/sonatype-nexus-community/jake/commit/1d2d8c67fd02e7a37868fa20fe7416add4558852))

* flail2 tox ([`3b65427`](https://github.com/sonatype-nexus-community/jake/commit/3b65427e6c847d7d13dbec857bc29e7c88e17f8d))

* flail tox ([`9e1e8c3`](https://github.com/sonatype-nexus-community/jake/commit/9e1e8c375722cc0a5908c7fd1a1585ba3db4337d))

* Missing return statement ([`43ba87e`](https://github.com/sonatype-nexus-community/jake/commit/43ba87ec13c43711eca7085fcd45f6e9c01d1865))

* Missing return statement ([`219059b`](https://github.com/sonatype-nexus-community/jake/commit/219059bef8057d030fe91a8634c24e070fa2de70))

* revert poetry ([`edab131`](https://github.com/sonatype-nexus-community/jake/commit/edab131e5bf2530c69e6d623156986001ae5cf82))

* revert poetry ([`798573f`](https://github.com/sonatype-nexus-community/jake/commit/798573fd21c3171ed99b20cadf7b44e3a6bb3288))

* vuln fix ([`5403087`](https://github.com/sonatype-nexus-community/jake/commit/540308701f0ff6d0c73b4667cd6cc8affec7adf3))

* vuln fix ([`d70881f`](https://github.com/sonatype-nexus-community/jake/commit/d70881f739cc318a3ab30b9020917aec725c00b5))

* tox ansi ([`7377f7b`](https://github.com/sonatype-nexus-community/jake/commit/7377f7bc0f5a04efaa973881b8f399dddc4b83f3))

* cleanup ([`681ea21`](https://github.com/sonatype-nexus-community/jake/commit/681ea216d3d42799b9d3a7999bd2373348e63e90))

* --no-ansi everywhere we install ([`1970be8`](https://github.com/sonatype-nexus-community/jake/commit/1970be8cdcd93f1a3a53090b5bc625179a5bd54d))

* -vvv --no-ansi ([`289d0d7`](https://github.com/sonatype-nexus-community/jake/commit/289d0d71e27aec55e990ea3242324b20cb6b5613))

* remove obsolete classifier ([`0bff856`](https://github.com/sonatype-nexus-community/jake/commit/0bff8566568c0ae4e43e7ff520808f41612d7d7d))

* revert requests ([`1b8df28`](https://github.com/sonatype-nexus-community/jake/commit/1b8df28f896720b5a98a6b6e5b611fa700d29cc8))

* by lock ([`1e72a3a`](https://github.com/sonatype-nexus-community/jake/commit/1e72a3a1f4fd938111b3fd5f409aa3cb0041c793))

* cache ([`8c94249`](https://github.com/sonatype-nexus-community/jake/commit/8c9424914b00b6324aed8e74a8736b96c54bd50e))

* poetry 1.5 ([`5c6cc2b`](https://github.com/sonatype-nexus-community/jake/commit/5c6cc2b26c618ab3ff7944f82a4026d0175ee4e0))

* flail2 ([`d3f5d4d`](https://github.com/sonatype-nexus-community/jake/commit/d3f5d4d36804738dcbcd9f136b7b1ae99d903bf7))

* flail ([`c90b651`](https://github.com/sonatype-nexus-community/jake/commit/c90b65184906904c47d44c4bab018eeeacdfe472))

* lift rug, sweep ([`838ab88`](https://github.com/sonatype-nexus-community/jake/commit/838ab882b579571609823f6b35b5984804671b4e))

* verbose install ([`71ba3bb`](https://github.com/sonatype-nexus-community/jake/commit/71ba3bb2239c7413cb729b67a1a633a5a0b1a51e))

* verbose install ([`e1fae4d`](https://github.com/sonatype-nexus-community/jake/commit/e1fae4d834824e32e47809338fee769c4e882fd3))

* newer poetry ([`6c23876`](https://github.com/sonatype-nexus-community/jake/commit/6c23876b3be87c817dd9bd71a256552b7e77321b))

* bad lock file? ([`733e02f`](https://github.com/sonatype-nexus-community/jake/commit/733e02f99e869b8cc88b7dabe43534f7ec8884f3))

* try cache busting ([`e1e3439`](https://github.com/sonatype-nexus-community/jake/commit/e1e3439d64b0a7d99213a568ea7c30d18f6579b1))

* remove python 3.6, require minimum python version 3.7. ([`396d806`](https://github.com/sonatype-nexus-community/jake/commit/396d806d0a1110d855d53dcfd701d7785df4de07))

* add missing license header ([`7aad2e2`](https://github.com/sonatype-nexus-community/jake/commit/7aad2e282176293d708c0b21fd293fabb792de24))

* revert fix: CVE-2022-23491 in certifi 2022.5.18.1, need to investigate other failures, waive violation while digging. ([`10ec0e1`](https://github.com/sonatype-nexus-community/jake/commit/10ec0e1f1d13ed678429546a66ae69d4ff6b0196))


## v3.0.0 (2022-12-02)

### Feature

* feat: Support for all input formats when running jake ddt or jake iq (#125)

* feat: Support for all input formats when running jake ddt or jake iq

closes #104

BREAKING CHANGE: changed iq -t switch to -st, use common `-f` argument for input file

Co-authored-by: Dan Rollo &lt;danrollo@gmail.com&gt; ([`9a597b5`](https://github.com/sonatype-nexus-community/jake/commit/9a597b59c7f3f042f7188a5cd6a7f6c8c0482f97))

### Fix

* fix: restore running jake on jake ([`675b359`](https://github.com/sonatype-nexus-community/jake/commit/675b35927a892755ec5fced019646c043ff3d671))

### Unknown

* revert add agentLabel ([`9f0bd52`](https://github.com/sonatype-nexus-community/jake/commit/9f0bd5230ce989463af3ad75750ce8fa1708843d))

* add agentLabel: &#39;ubuntu-zion-legacy&#39; to get build happy for now ([`ba16abe`](https://github.com/sonatype-nexus-community/jake/commit/ba16abe5a4aa87a741978181f0039a831995e75c))


## v2.1.1 (2022-06-09)

### Ci

* ci: temporarily removed running `jake` against `jake` as this is blocking release - likely due to OSS Index updates

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`88d390c`](https://github.com/sonatype-nexus-community/jake/commit/88d390c629cc1c2260745dabac3eb744f0448ea3))

### Unknown

* Merge pull request #120 from sonatype-nexus-community/fix/schema-version-argument-typo-117

fix: removed typo from default value of `--schema-version` argument #117 ([`738a00e`](https://github.com/sonatype-nexus-community/jake/commit/738a00e91897e2673037bb8656481e321cc7b695))


## v2.1.0 (2022-06-09)

### Chore

* chore: added unified license headers as per interal Sonatype check

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`ccb927b`](https://github.com/sonatype-nexus-community/jake/commit/ccb927b6441002107915cc82461bee80bc7e23c8))

### Ci

* ci: temporarily removed running `jake` against `jake` as this is blocking release - likely due to OSS Index updates

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`1da3571`](https://github.com/sonatype-nexus-community/jake/commit/1da3571e1cb2105cba7a65b9f2207ffbd741acca))

### Feature

* feat: add support for vulnerability whitelist when running `jake ddt` - thanks @daviskirk! ([`80e1136`](https://github.com/sonatype-nexus-community/jake/commit/80e113620642a032a767bd064ec317a7f19b7de1))

### Fix

* fix: removed typo from default value of `--schema-version` argument #117

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`e9e4764`](https://github.com/sonatype-nexus-community/jake/commit/e9e47649ab87eacdd0a98d8ee9798615d8913fdf))

### Unknown

* Add whitelisting support

* Add argument to dtt to support whitelisting via json file similar to auditjs ([`c81be03`](https://github.com/sonatype-nexus-community/jake/commit/c81be033052480b41a5bac140ca9885b79080d12))

* verify internal CI build success w/out tox ([`f428002`](https://github.com/sonatype-nexus-community/jake/commit/f428002bb3bb2776e8ae56eb468de980b331ef43))

* happyfy header checker (mostly newline after header, before import) - take 2 ([`84b4e11`](https://github.com/sonatype-nexus-community/jake/commit/84b4e11c64c3d59c8836487142b24a75e8b44f18))

* Revert &#34;happyfy header checker (mostly newline after header, before import)&#34;

This reverts commit 0afee0f145e0002817740e1345a98253794b251d. ([`9ee6125`](https://github.com/sonatype-nexus-community/jake/commit/9ee6125e47c3a6035bfc1e5a2f222bb43b7e9194))

* Revert &#34;happyfy header checker (mostly newline after header, before import)&#34;

This reverts commit 6a129a3acfb48c80732635a13f91d228de392fb2. ([`8f2a381`](https://github.com/sonatype-nexus-community/jake/commit/8f2a38168ae4623e4edcbeeb5601a21889e230bd))

* Merge branch &#39;main&#39; of github.com:sonatype-nexus-community/jake ([`8cfe403`](https://github.com/sonatype-nexus-community/jake/commit/8cfe403f388eaf8200d031cb232dbd1f4866c3e5))

* happyfy header checker (mostly newline after header, before import) ([`6a129a3`](https://github.com/sonatype-nexus-community/jake/commit/6a129a3acfb48c80732635a13f91d228de392fb2))

* happyfy header checker (mostly newline after header, before import) ([`0afee0f`](https://github.com/sonatype-nexus-community/jake/commit/0afee0f145e0002817740e1345a98253794b251d))

* doc: added OSS authentication configuration to documentation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`1230079`](https://github.com/sonatype-nexus-community/jake/commit/1230079b781a745f655ab2eb6ece7abcf895cb2e))


## v2.0.0 (2022-03-10)

### Breaking

* chore: bump to latest `cyclonedx-python`

BREAKING CHANGE: Notion of default schema version has been removed by upstream library and replaced with latest supported schema version

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`e437bb4`](https://github.com/sonatype-nexus-community/jake/commit/e437bb41ddbb84d7844f40b213878c67c071cc23))

### Feature

* feat: typing as per PEP-561 and other refactors (#114)

* feat: typing of `jake` WIP

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* port of fix for #112

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* resolved a bunch of typing issues

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* ci: fixed parameter references

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* ci: fixed parameter references

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* ci: fixed mypy

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* fix: updated `ossindex-lib` to latest RC which now appears to properly resolve caching issues #100

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* defined lowest dependencies and aligned

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* defined lowest dependencies and aligned

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* defined lowest dependencies and aligned

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* defined lowest dependencies and aligned

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* WIP: JSON output updated to use JSON serialisation
- All tests passing locally

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`a0ab7ee`](https://github.com/sonatype-nexus-community/jake/commit/a0ab7eecac96ea9dd1324117651556493247eb98))

### Fix

* fix: resolve historic oss index caching issues

feat: support for oss index authentication
Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`dc03aa9`](https://github.com/sonatype-nexus-community/jake/commit/dc03aa923cf2a8c48d0ad9e7e30cb188fb3a5a96))

### Unknown

* Merge pull request #109 from sonatype-nexus-community/dev

BREAKING CHANGE: Feature Release ([`398e70d`](https://github.com/sonatype-nexus-community/jake/commit/398e70d27113f82f82ad87f9e85480c6f9af204b))

* Merge branch &#39;main&#39; into dev ([`e2702ae`](https://github.com/sonatype-nexus-community/jake/commit/e2702aeb0857d116359603256d19f572318b975e))

* prevent manual_release job on non-main branches. partial fix for #108 (#115) ([`6a5fe46`](https://github.com/sonatype-nexus-community/jake/commit/6a5fe466696981d276d215b06707b379790af38b))


## v1.4.5 (2022-02-15)

### Chore

* chore: bumped dependencies (#107)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`2ee98fe`](https://github.com/sonatype-nexus-community/jake/commit/2ee98fea6453003b4581dbd02127009ae5b91a82))

### Feature

* feat: support for Python 3.10 (#110)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`671c8c4`](https://github.com/sonatype-nexus-community/jake/commit/671c8c4bb682b4b944568198ecf381818d49f3ac))

### Fix

* fix: pin some upstream dependencies to prevent #112 (#113)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`8a43e0a`](https://github.com/sonatype-nexus-community/jake/commit/8a43e0af074f797abaddcc0a542b5e08d8a75b36))

### Unknown

* doc: first pass at docs for RTD (#111)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`223978f`](https://github.com/sonatype-nexus-community/jake/commit/223978f94e43f69ee47a9db80e9542accc2646fe))


## v1.4.4 (2022-02-08)

### Fix

* fix: CWEs are `int` and needed to be stringified (#102)

fix: Vulnerability rating score now formatted to 1 decimal place

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`3e15cb1`](https://github.com/sonatype-nexus-community/jake/commit/3e15cb16c037d8bb09eb5c38dbd239dd345f09cc))


## v1.4.3 (2022-02-03)

### Fix

* fix: CWEs not passed as ints to CDX model (#97)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`6ec49a6`](https://github.com/sonatype-nexus-community/jake/commit/6ec49a6a7d2b22b2535346409ee49fc3cd5f2c8b))


## v1.4.2 (2022-01-31)

### Fix

* fix: corrected data placement for Vulnerabilities returned from OSS Index when generating an SBOM (#94)

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`eb12286`](https://github.com/sonatype-nexus-community/jake/commit/eb1228602c63784da751749cce14ee9fec9f3d1f))


## v1.4.1 (2022-01-24)

### Fix

* fix: `bom-ref` will always now be populated for Component and Vulnerability - bump of `cyclonedx-python-lib` solves this (#92)

fix: complete `affects` for vulnerabilities received from OSS Index

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`df2aad2`](https://github.com/sonatype-nexus-community/jake/commit/df2aad2fa23548e98d2857e2f038e4850067f9b6))

### Unknown

* sooth license header check ([`4163708`](https://github.com/sonatype-nexus-community/jake/commit/41637088c490ed59c0b0abef802513cf1293f522))

* try to get a test running (#89)

* try to get a test running. 
* change tox.ini testenv command to work with current layout ([`86afdb5`](https://github.com/sonatype-nexus-community/jake/commit/86afdb5848f020777bb8587f6ac7be44d6f523bb))

* [skip ci] add license header (newline after header) ([`4cde312`](https://github.com/sonatype-nexus-community/jake/commit/4cde3125dc67c206b00b03851a02540b607e109b))

* [skip ci] add license header ([`fddd1a7`](https://github.com/sonatype-nexus-community/jake/commit/fddd1a7f438eedc02ed405333522df6471c7d6f3))


## v1.4.0 (2022-01-13)

### Feature

* feat: support CycloneDX 1.4 (#87)

* fix: unified how current version of `jake` is collected

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* feat: adopted latest RC for CycloneDX libraries to enable 1.4 support

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* fixes

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt;

* chore: bumped to released versions of CyloneDX libraries`

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`20c62fc`](https://github.com/sonatype-nexus-community/jake/commit/20c62fcb70d1245e5c31df56ad3d71bc9e7fe0d0))

### Unknown

* doc: updated to reflect first version with pre-commit config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`8360771`](https://github.com/sonatype-nexus-community/jake/commit/83607715c545e8526c430a60a9f1574fc34f85e0))


## v1.3.0 (2022-01-11)

### Feature

* feat(pre-commit): add pre-commit hooks (#85) ([`45f108e`](https://github.com/sonatype-nexus-community/jake/commit/45f108e018925f932768f29855b19342fcec2ac1))


## v1.2.3 (2021-12-22)

### Fix

* fix: resolved regression when running `jake ddt` where return code != 0 when vulnerabilities discovered

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`8a10e70`](https://github.com/sonatype-nexus-community/jake/commit/8a10e700cea51b649ef7f2271a44e42109264e9a))


## v1.2.2 (2021-12-15)

### Fix

* fix: removed a number of direct dependencies that are now transitives, or no longer required
fix: relaxed version requirements for remaining dependencies

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`bcb0a3d`](https://github.com/sonatype-nexus-community/jake/commit/bcb0a3d222c23f88e92fc74c37fd2864e236d8d5))

### Unknown

* Merge pull request #81 from sonatype-nexus-community/feat/relax-and-tidy-dependencies

fix: addressed dependency review #73 ([`dbe5d31`](https://github.com/sonatype-nexus-community/jake/commit/dbe5d313f29cb75f004fefc4f0cdb902ad630273))


## v1.2.1 (2021-12-15)

### Ci

* ci: disabled GitHub Workflows as per #76

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`08fd4a4`](https://github.com/sonatype-nexus-community/jake/commit/08fd4a47c0b3d9b8fea7217e894dda61294ac9a7))

### Fix

* fix: bumped dependencies to resolve wheel-only installation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`4ac980d`](https://github.com/sonatype-nexus-community/jake/commit/4ac980d0d7696128e03f982de2dabdfaf7009e03))

### Unknown

* Merge pull request #80 from sonatype-nexus-community/fix/install-from-wheels-only

fix: bumped dependencies to resolve wheel-only installation ([`9458d3b`](https://github.com/sonatype-nexus-community/jake/commit/9458d3bbefced8fc82b12bd4e7b81185cf29aa1f))

* Merge pull request #79 from sonatype-nexus-community/feat/remove-github-actions

ci: disable GitHub Workflows as per #76 ([`d5af310`](https://github.com/sonatype-nexus-community/jake/commit/d5af310a6d835524307dab923366866a5dc52ce8))


## v1.2.0 (2021-12-13)

### Chore

* chore: resolved merge in from master

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`3ba93e3`](https://github.com/sonatype-nexus-community/jake/commit/3ba93e3d58aa495d81b5c19271f48790b4608d84))

### Feature

* feat: replaced `yaspin`, `termcolor` and `terminaltable` with `rich` - see #72, #73, #77

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`8534ad9`](https://github.com/sonatype-nexus-community/jake/commit/8534ad92acf6b70407492e55ec68ede3190a393b))

* feat: removed `terminaltables` and replaced with `rich`s table implementation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`416b03c`](https://github.com/sonatype-nexus-community/jake/commit/416b03c0c844a28512143826453ad956e98abd7c))

* feat: removed `yaspin` and replaced with `rich`

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`76c4a54`](https://github.com/sonatype-nexus-community/jake/commit/76c4a5451e04c28612ab3c034bbd4a84fa413c94))

### Fix

* fix: removed f-strings as not required

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`b5b271e`](https://github.com/sonatype-nexus-community/jake/commit/b5b271ed78b97101e9fca2e31b2789540bf66fd4))

### Unknown

* Merge pull request #78 from sonatype-nexus-community/feat/replace-yaspin-with-rich

feat: removed `yaspin` and replaced with `rich` ([`eb69be0`](https://github.com/sonatype-nexus-community/jake/commit/eb69be04bd7a4cfc49012c5df445050af61dc332))

* doc: updated README

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`99c83ee`](https://github.com/sonatype-nexus-community/jake/commit/99c83eee6fe7d57f88311f6fea99182836b2961d))

* removed unused improt

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`d02fef3`](https://github.com/sonatype-nexus-community/jake/commit/d02fef3c6ccc26482c9ac7de8a9aeb989495fe05))


## v1.1.5 (2021-12-09)

### Fix

* fix: bump required version of cyclonedx-python-lib to help lax transitive dependencies ([`f53407f`](https://github.com/sonatype-nexus-community/jake/commit/f53407fb72625420f015db59bb801cc12ab290cf))

* fix: bump required version of cyclonedx-python-lib to help lax transitive dependencies

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`34e501d`](https://github.com/sonatype-nexus-community/jake/commit/34e501d062da5607f86879e136d1f988de6dd872))


## v1.1.4 (2021-12-07)

### Ci

* ci: update CI to only install binary packages

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`63acf2c`](https://github.com/sonatype-nexus-community/jake/commit/63acf2c20c143c958a1457756d7002a29491f9f3))

### Fix

* fix: ensure dependencies can be installed from binary packages #72

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`9e30ca8`](https://github.com/sonatype-nexus-community/jake/commit/9e30ca8d11bc6ee578749686ff3af30b1c805b10))

### Unknown

* Merge pull request #74 from sonatype-nexus-community/feat/wheel-only-installation

fix: ensure dependencies can be installed from binary packages #72 ([`55fd644`](https://github.com/sonatype-nexus-community/jake/commit/55fd64430276993dc2e5c5850e7c7e564d54782f))

* revert CI changes as these fail ([`d82ff22`](https://github.com/sonatype-nexus-community/jake/commit/d82ff2207ffd58843fa9f433e447f53de73f2d68))

* doco typos ([`e11b560`](https://github.com/sonatype-nexus-community/jake/commit/e11b56005d070b17fa101c5fe86e3b6a38d7c2dc))

* Merge branch &#39;main&#39; of github.com:sonatype-nexus-community/jake ([`091b4e9`](https://github.com/sonatype-nexus-community/jake/commit/091b4e90aeb19d9d81de0379b3e59eedee23ea2e))

* add doco about required comment prefix for a release to be generated ([`839be7c`](https://github.com/sonatype-nexus-community/jake/commit/839be7ca10512ad12410d72c3f81b7b0298b9cd7))


## v1.1.3 (2021-11-10)

### Fix

* fix: return exit code up the call stack ([`12caad2`](https://github.com/sonatype-nexus-community/jake/commit/12caad22e2c5bca95d4f2a4bafae5b95b4a7fd2a))

### Unknown

* return exit code up the call stack ([`193b2b4`](https://github.com/sonatype-nexus-community/jake/commit/193b2b4c3fa3a085a70d9368ebf7a4d81dce4cd7))

* run IQ using &#39;release&#39; stage to trigger policy failure actions ([`bc2d362`](https://github.com/sonatype-nexus-community/jake/commit/bc2d36290efbb55fcae830db450548320529f5e7))


## v1.1.2 (2021-11-10)

### Fix

* fix: restore &#34;stage&#34; parameter for iq command, for realsies ([`f1d8c64`](https://github.com/sonatype-nexus-community/jake/commit/f1d8c64853c707ccd07dcceb5bd04bffbd4078db))

### Unknown

* use iq.sonatype.dev, new server, new credentials ([`46c2979`](https://github.com/sonatype-nexus-community/jake/commit/46c29795e14d8c9367f1624e7d6b86a2953fa750))

* use iq.sonatype.dev ([`2eba0f9`](https://github.com/sonatype-nexus-community/jake/commit/2eba0f985e19c1631e3c6a17d86e6968e2709e2a))


## v1.1.1 (2021-11-09)

### Fix

* fix: restore &#34;stage&#34; parameter for iq command ([`01a41da`](https://github.com/sonatype-nexus-community/jake/commit/01a41dae1ca8f13d7f3837f695daa25792f9e834))

### Unknown

* doco: manual release ([`0f65a10`](https://github.com/sonatype-nexus-community/jake/commit/0f65a10f2e036a9d9b3d6c0d4b178e8630409a8b))

* doco: restore &#34;releasing&#34; doco, will try it out momentarily. ([`fd2fba9`](https://github.com/sonatype-nexus-community/jake/commit/fd2fba9eb1d9361b40a421f45c4d9391e92e96db))

* doco: restore &#34;stage&#34; parameter for iq command ([`10c8efd`](https://github.com/sonatype-nexus-community/jake/commit/10c8efdc33b0c56050e31ff48159e09248412607))

* restore &#34;stage&#34; parameter for iq command ([`a82aef2`](https://github.com/sonatype-nexus-community/jake/commit/a82aef2df0fdca725ba912b5c4e3e0fb8e75ae7f))

* typo ([`d0faf4b`](https://github.com/sonatype-nexus-community/jake/commit/d0faf4be60d0c6e279e3fc454a1cfb804843be1d))

* chain commands ([`42b245d`](https://github.com/sonatype-nexus-community/jake/commit/42b245da7639d2f055c898a017bb5ca87398e0bc))

* iq arg name change ([`1f5e6f5`](https://github.com/sonatype-nexus-community/jake/commit/1f5e6f567714baa9bd364c6f05509f5f5a235209))

* scan jake with jake ([`5b831bd`](https://github.com/sonatype-nexus-community/jake/commit/5b831bd98c3303a03b3ad9a56890775af3378165))

* scan jake with jake ([`fb892d2`](https://github.com/sonatype-nexus-community/jake/commit/fb892d2b43003e044347b3642ec8293fbf106611))

* happy headers, now the build... ([`1120d8a`](https://github.com/sonatype-nexus-community/jake/commit/1120d8a3b782ff581ea0b661f83a65290bcee381))

* header checker appeasement - wonder if this will work with .ini format... ([`521ff5d`](https://github.com/sonatype-nexus-community/jake/commit/521ff5d5c5ebf2178316475d6156132425636672))

* header checker appeasement ([`9d9d78e`](https://github.com/sonatype-nexus-community/jake/commit/9d9d78e0876573f5d74b81c183b930b389fdfd00))

* revert unused files - restore license-excludes.xml ([`43c73e7`](https://github.com/sonatype-nexus-community/jake/commit/43c73e70e8b27fe837a81b10248a0c22e8be66b8))

* revert unused files - restore header.txt ([`560e516`](https://github.com/sonatype-nexus-community/jake/commit/560e5163e57960bdbc9812e3fef39e26da7ebc20))

* revert unused files - restore Jenkinsfile ([`719b914`](https://github.com/sonatype-nexus-community/jake/commit/719b9144bcc2a2152b459b13cd4342753d94ab13))


## v1.1.0 (2021-10-22)

### Feature

* feat: add support for conda #66
fix: character encoding issues on Windows #67

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`a3495cb`](https://github.com/sonatype-nexus-community/jake/commit/a3495cb55fe835181ae57a1a48b9ff8cbe7b7415))

### Unknown

* Merge pull request #70 from sonatype-nexus-community/feat/conda-support

FEATURE: `conda` support + fixes ([`93bc03d`](https://github.com/sonatype-nexus-community/jake/commit/93bc03dee13f941525536005c9dd9de1176d4285))

* doc: typo resolved

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`286ea27`](https://github.com/sonatype-nexus-community/jake/commit/286ea276f61b719343a2eaef7fce00ce8d9c7ab5))

* doc: update README to cover updated paramters and conda support

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`7d9274f`](https://github.com/sonatype-nexus-community/jake/commit/7d9274fc16d53b0ae9117be77520d66fcd6361b7))

* Updated config.yml ([`b1cfcb4`](https://github.com/sonatype-nexus-community/jake/commit/b1cfcb46796c3c285197d5c2c70d4a0061742b72))


## v1.0.1 (2021-10-20)

### Fix

* fix: update to support returning non-zero exit code when issues found (will return 1)
fix: incorrect check for Nexus IQ policy Warnings remediated

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`7667bac`](https://github.com/sonatype-nexus-community/jake/commit/7667bacb171803f7963bec12240520985103d06c))

### Unknown

* Merge pull request #69 from sonatype-nexus-community/fix/issue-65-exit-code

FIX: Enable non-zero exit code + correct logic in determining Nexus IQ policy warnings ([`7b6122b`](https://github.com/sonatype-nexus-community/jake/commit/7b6122beafa6dec72da793fc9185cbc9b1bd6a33))


## v1.0.0 (2021-10-18)

### Breaking

* refactor: re-write to consume new cyclonedx-python-lib

BREAKING CHANGE: `jake` has been re-written in large part to consume two new external libraries:
- `cyclonedx-python-lib` which gives `jake` ability to more easily consume your depenedencies in a variety of manners (environment, Pipfile.lock, poetry.lock, requirements.txt) and support output in both JSON and XML at different schema versions
- `ossindex-lib`: most of the functionallity for talking to OSS Index that was in `jake` has been externalised to this library to allow others to consume it

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`e11cb20`](https://github.com/sonatype-nexus-community/jake/commit/e11cb208c215169d6ce24fa8898a5aa2402d8791))

### Build

* build: now using officially published version of ossindex-lib

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`5241427`](https://github.com/sonatype-nexus-community/jake/commit/5241427ffa542f650c776de3d727759b4c0a1916))

### Ci

* ci: attempt to get semantic-release running on CircleCI

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`1e610e1`](https://github.com/sonatype-nexus-community/jake/commit/1e610e1795e29102e7b5816124d8cd215d58f49a))

* ci: aligned to previous CircleCI context

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`f8e9833`](https://github.com/sonatype-nexus-community/jake/commit/f8e98337ee61134681490d2318d05ec4172d4ea1))

* ci: use CircleCI context for PYPI_TOKEN and re-introduced SSH key to attempt to resolve GitHub connectivity during release

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`26621ac`](https://github.com/sonatype-nexus-community/jake/commit/26621ac212cc1b72e76c58f78ebeb58452c52141))

* ci: disable Release Job on CircleCI and move back to GitHub Action

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`6ebb6df`](https://github.com/sonatype-nexus-community/jake/commit/6ebb6df80d8813fb92456b9ca500a97f1707bdf6))

* ci: alternative attempt to set Git Author

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`5773199`](https://github.com/sonatype-nexus-community/jake/commit/577319906c17ce202d2eb415714f091438c97325))

* ci: alternative attempt to set Git Author

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`bdc0931`](https://github.com/sonatype-nexus-community/jake/commit/bdc093171a4aed22489b57cdc0a8e0b4b62f8f1a))

* ci: defined commit_author for semantic-release

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`d0dcf15`](https://github.com/sonatype-nexus-community/jake/commit/d0dcf15d8bc9c21178fb7a739531a79f25fdccd2))

* ci: fix cache key for release CircleCI job

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`a730e9e`](https://github.com/sonatype-nexus-community/jake/commit/a730e9e27ba52b1fe27263161296457d57f8b995))

* ci: update CircleCI release to run on every commit to main

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`a5fc8b8`](https://github.com/sonatype-nexus-community/jake/commit/a5fc8b899142bc7e8818e07328616c6413553a11))

* ci: disabled GitHub Action for deployment

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`daebf39`](https://github.com/sonatype-nexus-community/jake/commit/daebf399b76db27c6d5207ac8ce233878f626b0e))

* ci: remove --noop from semantic-release

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`e41a7a2`](https://github.com/sonatype-nexus-community/jake/commit/e41a7a2825b8c6101805c2838709384d86a20a5a))

* ci: further work on CircleCI config

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`bc42408`](https://github.com/sonatype-nexus-community/jake/commit/bc424085efc64f9a39a2ed3ee50ba76376f7f5be))

* ci: re-introduce CircleCI with updated implementation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`59c6b62`](https://github.com/sonatype-nexus-community/jake/commit/59c6b62030e37ac74ce997756339833acac0ed1e))

* ci: move from CircleCI to GitHub actions

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`6d73b10`](https://github.com/sonatype-nexus-community/jake/commit/6d73b10ef6bd6ccea90f9e1f0e34348b09dfe59f))

### Feature

* feat: Sonatype Nexus IQ Lifecycle analysis is now migrated to using cyclonedx-python-lib

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`214d182`](https://github.com/sonatype-nexus-community/jake/commit/214d1821fa94ff895a2bfa4eac0f6961df093f46))

* feat: support Poetry for gleaning packages within the current environment to generate an SBOM

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`b9a1e5d`](https://github.com/sonatype-nexus-community/jake/commit/b9a1e5d2f38963a033d102399827c5c4dfe786da))

* feat: jake&#39;s OSS calls now utilising ossindex-lib and cyclonedx-python-lib

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`ec83583`](https://github.com/sonatype-nexus-community/jake/commit/ec83583520aa5ff8180b215b55846ed7a6fd487c))

### Fix

* fix: additional whitespace removed

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`709f7a2`](https://github.com/sonatype-nexus-community/jake/commit/709f7a2aa752668daba99c04b36ad9b8a6d271f2))

* fix: runtime tweaks to make it more robust

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`13c9028`](https://github.com/sonatype-nexus-community/jake/commit/13c902838008377e11e4c47ed619401776b8f782))

* fix: typos noted as updating documentation

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`0d65116`](https://github.com/sonatype-nexus-community/jake/commit/0d65116a17757b1ccf4c73bc463ee677eef0d5ff))

### Refactor

* refactor: removed unused files

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`82492b3`](https://github.com/sonatype-nexus-community/jake/commit/82492b35f20b4da74243890f59a603adb552e7eb))

* refactor: removing old Jake code superseded by cyclonedx-python-lib and ossindex-lib

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`d8941f5`](https://github.com/sonatype-nexus-community/jake/commit/d8941f57575ab2cb0d2e334ce546cf11af8ab63a))

### Unknown

* revert patch arg ([`58b3aa0`](https://github.com/sonatype-nexus-community/jake/commit/58b3aa024bfc61ac475d5b9ec45e1723d5a53f67))

* make publish a manual process for now. update circleci docs. ([`f5b2d42`](https://github.com/sonatype-nexus-community/jake/commit/f5b2d42afa8a6b179c674a1a4642e90f514c7ad4))

* try patch publish ([`28dd92f`](https://github.com/sonatype-nexus-community/jake/commit/28dd92f47f7c57d69bef8af85008466d54bd082f))

* Merge pull request #64 from madpah/feature/update-to-use-cyclonedx-python-lib

Migrate `jake` to utilise external CycloneDX and OSSIndex libraries ([`2fff773`](https://github.com/sonatype-nexus-community/jake/commit/2fff773c8d130ebb2bf87c2f1e2ea59c362678a3))

* doc: README updated to cater for refactorings

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`7ed4f4e`](https://github.com/sonatype-nexus-community/jake/commit/7ed4f4eb7a37adc90770fe7ff6f5a7e97be0af5f))

* wip: migrating Jake to use cyclonedx-python-lib and ossindex-lib

Signed-off-by: Paul Horton &lt;phorton@sonatype.com&gt; ([`23f6412`](https://github.com/sonatype-nexus-community/jake/commit/23f6412a3655ed19b0aed2ead21d6c35535e3fd1))


## v0.2.77 (2021-07-06)

### Fix

* fix: CVE-2021-33503 in urllib3 == 1.26.4 (#62) ([`9dfbb1c`](https://github.com/sonatype-nexus-community/jake/commit/9dfbb1c18831a1456803299e2f98a95ba95ea2b8))

### Unknown

* 0.2.77

[skip ci] ([`fc2ecb1`](https://github.com/sonatype-nexus-community/jake/commit/fc2ecb17303943cd9dba28383fc062f5700028c3))


## v0.2.76 (2021-06-29)

### Fix

* fix: &#34;ModuleNotFoundError: No module named &#39;typing_extensions&#39;&#34;, occurring in &#39;python3.7/site-packages/tinydb/queries.py&#34;, line 28&#39; on Jenkins CI (#61) ([`a747750`](https://github.com/sonatype-nexus-community/jake/commit/a7477505a0e6d1b198461a75ef8d755cc37dfe12))

### Unknown

* 0.2.76

[skip ci] ([`029cbb4`](https://github.com/sonatype-nexus-community/jake/commit/029cbb4b71553c3954e346bc475bb4d6ccd92b2f))

* Revert &#34;attempt to fix: ModuleNotFoundError: No module named &#39;typing_extensions&#39;, occurring in &#39;python3.7/site-packages/tinydb/queries.py&#34;, line 28&#39; on Jenkins CI [skip ci]&#34;

This reverts commit e867ec78 ([`135b675`](https://github.com/sonatype-nexus-community/jake/commit/135b67559c8c3ecfc9cf3162391e00b9495d0043))

* attempt to fix: ModuleNotFoundError: No module named &#39;typing_extensions&#39;, occurring in &#39;python3.7/site-packages/tinydb/queries.py&#34;, line 28&#39; on Jenkins CI [skip ci] ([`e867ec7`](https://github.com/sonatype-nexus-community/jake/commit/e867ec78237e9b5cd58c95aa06adbd385e3acbc0))

* Revert &#34;attempt to fix: ModuleNotFoundError: No module named &#39;typing_extensions&#39;, occurring in &#39;python3.7/site-packages/tinydb/queries.py&#34;, line 28&#39; on Jenkins CI [skip ci]&#34;

This reverts commit 1e25b8ea ([`83d948f`](https://github.com/sonatype-nexus-community/jake/commit/83d948f6485dad8bb1419e6e26bc3d191a010007))

* attempt to fix: ModuleNotFoundError: No module named &#39;typing_extensions&#39;, occurring in &#39;python3.7/site-packages/tinydb/queries.py&#34;, line 28&#39; on Jenkins CI [skip ci] ([`1e25b8e`](https://github.com/sonatype-nexus-community/jake/commit/1e25b8ea5778321da1602c9536fd0995a01803e2))


## v0.2.75 (2021-05-25)

### Unknown

* 0.2.75

[skip ci] ([`fcdfe57`](https://github.com/sonatype-nexus-community/jake/commit/fcdfe573b7cf78559ea8a0d03abfe857d44ab7d5))

* call ci-setup.sh before publishing to ensure non-dev virtual env exists. ([`1e1c6b0`](https://github.com/sonatype-nexus-community/jake/commit/1e1c6b0be032d5c1dac8c93bc3a8b15bacf2ecd3))

* move dev dependencies out of requirements.txt (#59)

* move more dev requirements ([`171e440`](https://github.com/sonatype-nexus-community/jake/commit/171e440a9468331026a55e43dc42561e0761609a))


## v0.2.74 (2021-05-25)

### Unknown

* 0.2.74

[skip ci] ([`d9849b6`](https://github.com/sonatype-nexus-community/jake/commit/d9849b6c01c45a94f7009bc5478b7241947ab5ed))

* Add json output format for ddt command (#56)

* add support for reading dependecies from pip requirements file ([`aa36e9f`](https://github.com/sonatype-nexus-community/jake/commit/aa36e9f2ed09193c2121a791c237ff96f3a83c3f))


## v0.2.73 (2021-05-25)

### Unknown

* 0.2.73

[skip ci] ([`e73d9eb`](https://github.com/sonatype-nexus-community/jake/commit/e73d9ebb6fdd6b635eeb074d7666f62b60c0a8a5))

* Add support for reading dependecies from pip requirements file (#55)

* add support for reading dependecies from pip requirements file ([`542d94a`](https://github.com/sonatype-nexus-community/jake/commit/542d94a0b782e51684042ec6c38b69a9997e7397))


## v0.2.72 (2021-05-13)

### Fix

* fix: Inline targets help changes (#58)

* added example to readme of site-packages target list generation in-line to the flag argument

* added site-packages one-liner to -t help description and updated readme to include an example invocation ([`c146a7d`](https://github.com/sonatype-nexus-community/jake/commit/c146a7d87e0859040b01278de8a2d09eb9b8b1cb))

### Unknown

* 0.2.72

[skip ci] ([`6f833ba`](https://github.com/sonatype-nexus-community/jake/commit/6f833ba9aa0e0488e8dfdf540c11d7e70424bd17))


## v0.2.71 (2021-05-13)

### Fix

* fix: #49 allow newer version of dependencies (#57)

* fix: #49 allow newer version of dependencies, click lib had issues. fix db call.
* lockdown development dependency versions ([`15553d4`](https://github.com/sonatype-nexus-community/jake/commit/15553d43932feca9978931734cf70c655158417d))

### Unknown

* 0.2.71

[skip ci] ([`92c9917`](https://github.com/sonatype-nexus-community/jake/commit/92c991794cb7a7423540ea66f212635cc3c37168))


## v0.2.70 (2021-04-07)

### Fix

* fix: CVE-2020-14343 in PyYAML==5.3.1 ([`11dc3c9`](https://github.com/sonatype-nexus-community/jake/commit/11dc3c90a2df876e2cda02be33a38c5f2a0c3fc4))

### Unknown

* 0.2.70

[skip ci] ([`f60f251`](https://github.com/sonatype-nexus-community/jake/commit/f60f25134c64c3e7d3426546913daec1837aeb47))


## v0.2.69 (2021-03-25)

### Fix

* fix: CVE-2021-28957 in lxml==4.6.2 ([`6d4373c`](https://github.com/sonatype-nexus-community/jake/commit/6d4373cd8fe320a17d3f8ca95208a0d5b38888ee))

### Unknown

* 0.2.69

[skip ci] ([`c2c9004`](https://github.com/sonatype-nexus-community/jake/commit/c2c9004e3a15fcb2cc6530f47f7b4044f89d140b))


## v0.2.68 (2021-03-23)

### Unknown

* 0.2.68

[skip ci] ([`9505ed2`](https://github.com/sonatype-nexus-community/jake/commit/9505ed2d1a9eee18d5db3b9cbab3a2edcd99ed78))

* extract common executor ([`a671abd`](https://github.com/sonatype-nexus-community/jake/commit/a671abda744707e16680573ce823b1543e794396))


## v0.2.67 (2021-03-18)

### Unknown

* 0.2.67

[skip ci] ([`62be893`](https://github.com/sonatype-nexus-community/jake/commit/62be893d345792f1748aec8dec87c3f4b2e39e2b))

* upgrade urllib3 to fix CVE-2021-28363 (#52) ([`eb2fead`](https://github.com/sonatype-nexus-community/jake/commit/eb2feadb3aacd631985629fe2a17265a5d62c4ea))


## v0.2.66 (2021-02-11)

### Unknown

* 0.2.66

[skip ci] ([`49550f2`](https://github.com/sonatype-nexus-community/jake/commit/49550f2aa4fcf145e6f449d6dfe1cc43ca68d2cb))

* stagger cron time ([`0c8cc27`](https://github.com/sonatype-nexus-community/jake/commit/0c8cc27e43d321692ee49882282c14a0421a3564))


## v0.2.65 (2021-01-27)

### Unknown

* 0.2.65

[skip ci] ([`3b7f2d0`](https://github.com/sonatype-nexus-community/jake/commit/3b7f2d0dfe3e78ff768a26394689180108a86ba2))

* use an absolute report url (handle IQ 104+) (#48)

* use an absolute report url (handle IQ 104+) ([`2cac53e`](https://github.com/sonatype-nexus-community/jake/commit/2cac53e768bf94ac7e4b1498018287c1f0be1fac))


## v0.2.64 (2020-12-17)

### Unknown

* 0.2.64

[skip ci] ([`5377f24`](https://github.com/sonatype-nexus-community/jake/commit/5377f248b82cb523f79a7cb92be769f3b5d15569))

* use link to raw logo file - avoid 302, 304 redirect ([`3b9a2df`](https://github.com/sonatype-nexus-community/jake/commit/3b9a2df6587eb36396907997f8d2163152dd00f0))


## v0.2.63 (2020-12-17)

### Unknown

* 0.2.63

[skip ci] ([`29b8ef1`](https://github.com/sonatype-nexus-community/jake/commit/29b8ef1804883fca8aaa73f2de39ef9d292f780d))

* try svg logo for pypi ([`95e4aec`](https://github.com/sonatype-nexus-community/jake/commit/95e4aecd493abab258fcf395ff337e7e94c9df74))


## v0.2.62 (2020-12-17)

### Unknown

* 0.2.62

[skip ci] ([`4737676`](https://github.com/sonatype-nexus-community/jake/commit/4737676077295301ec4cf4865ba926bdb16c34d7))

* show logo on pypi.org pages (#46)

* simplify logo markdown so it will show on pypi.org pages
* use smaller Jake logo ([`67d460b`](https://github.com/sonatype-nexus-community/jake/commit/67d460b63b1286f721b2ef08b51bc2bfee25f4cc))


## v0.2.61 (2020-12-17)

### Unknown

* 0.2.61

[skip ci] ([`ce6dc87`](https://github.com/sonatype-nexus-community/jake/commit/ce6dc879ce3872c41398daeed42f180dc8d95a4c))

* exclude SECURITY.md from license check in internal build ([`87e8662`](https://github.com/sonatype-nexus-community/jake/commit/87e866293b00e93d5499c07ed5b76eff9bd2de71))


## v0.2.60 (2020-12-16)

### Unknown

* 0.2.60

[skip ci] ([`6a3ac80`](https://github.com/sonatype-nexus-community/jake/commit/6a3ac80682dcb05fa111b317079dfbdafe492a40))

* updated SECURITY.md (#47) ([`f76e378`](https://github.com/sonatype-nexus-community/jake/commit/f76e37889081bb7a5c9e4ae802747d3b8aa3cccd))

* [skip ci] typos ([`9496dc1`](https://github.com/sonatype-nexus-community/jake/commit/9496dc1038a562f86cf3b1bd273ec786a885fa38))


## v0.2.59 (2020-12-09)

### Fix

* fix: Resolve vulnerability: CVE-2020-27783 in lxml ([`7526728`](https://github.com/sonatype-nexus-community/jake/commit/7526728623e102fb75fad30eb82be8824abbdf39))

### Unknown

* 0.2.59

[skip ci] ([`49d1693`](https://github.com/sonatype-nexus-community/jake/commit/49d169340911b393054ea44da2097bea1bf74283))

* [skip ci] fix pep violation ([`383ec1b`](https://github.com/sonatype-nexus-community/jake/commit/383ec1bf1d9239434716582fab900a8208e1f377))

* [skip ci] doc pip3 ([`7a6880b`](https://github.com/sonatype-nexus-community/jake/commit/7a6880bc96dd5909dfec8fd8a84989b2d27e916c))

* [skip ci] do not print &#34;Non-Vulnerable Dependencies&#34; header when running in quiet mode ([`3d95ba9`](https://github.com/sonatype-nexus-community/jake/commit/3d95ba91f604e53d83a6cc9d72cb071f61475df8))

* [skip ci] use iq appId &#39;sandbox-application&#39; in example ([`87d5019`](https://github.com/sonatype-nexus-community/jake/commit/87d5019e9faede075f4874609559c96f86721b36))

* [skip ci] fix usage text ([`31034a0`](https://github.com/sonatype-nexus-community/jake/commit/31034a0c8c1c6446ac2322eba2982a0ce01b4579))

* [skip ci] provide alt attribute ([`e41806c`](https://github.com/sonatype-nexus-community/jake/commit/e41806c9ea9455dd95bcbcd7c6f85b67574fd26d))

* [skip ci] doc release process ([`33c9dd0`](https://github.com/sonatype-nexus-community/jake/commit/33c9dd015485a563c9d296d5d657730268dfe65b))

* [skip ci] typo ([`ec96fa4`](https://github.com/sonatype-nexus-community/jake/commit/ec96fa452ab964ee21f32a80412612b562f494f0))


## v0.2.58 (2020-12-07)

### Unknown

* 0.2.58

[skip ci] ([`4da1866`](https://github.com/sonatype-nexus-community/jake/commit/4da1866b7d35fcae47f85575488704c224549f72))

* revert &#34;quiet&#34; by default, avoid disabling std.out ([`614f762`](https://github.com/sonatype-nexus-community/jake/commit/614f762bc99794ec62411727e9016dc434eb9a4d))

* &#34;quiet&#34; by default, fix verbose error message hint ([`e946ef9`](https://github.com/sonatype-nexus-community/jake/commit/e946ef95c6b839089a298a6dcc2a552eb2218ee6))


## v0.2.57 (2020-11-12)

### Unknown

* 0.2.57

[skip ci] ([`0812781`](https://github.com/sonatype-nexus-community/jake/commit/0812781bbb68c18c751debde954592862cffa54d))

* fix doc links ([`e23bb78`](https://github.com/sonatype-nexus-community/jake/commit/e23bb7881b3ce909bcfb00e98c06f6a8c4d79a8c))


## v0.2.56 (2020-11-12)

### Unknown

* 0.2.56

[skip ci] ([`cbd9223`](https://github.com/sonatype-nexus-community/jake/commit/cbd922331fcbe478cc0adc882c835593f4991d52))

* resolve issue: sonatype-2020-1076 via updated lxml, and friends. ([`007d671`](https://github.com/sonatype-nexus-community/jake/commit/007d671ce910968b6edbb317e821ad22ac658c44))

* Document internal build files. ([`0303c41`](https://github.com/sonatype-nexus-community/jake/commit/0303c4125c854c54586c93ade136dda2b569109f))


## v0.2.55 (2020-11-12)

### Unknown

* 0.2.55

[skip ci] ([`ddef852`](https://github.com/sonatype-nexus-community/jake/commit/ddef8521401ead808402388afa2612fee6e8f5cf))

* yes, do the dev-requirements uninstall ([`42a41a7`](https://github.com/sonatype-nexus-community/jake/commit/42a41a740453283739a01ffb5274fd8e08654561))


## v0.2.54 (2020-11-12)

### Unknown

* 0.2.54

[skip ci] ([`98ac471`](https://github.com/sonatype-nexus-community/jake/commit/98ac471184ff20b4ae1c4d9d611ab0cd8bbdd580))

* Merge branch &#39;main&#39; of github.com:sonatype-nexus-community/jake into main ([`076baa3`](https://github.com/sonatype-nexus-community/jake/commit/076baa3d7b871a4ac723f6a537b0c1ba5dd7388b))

* try removing dev requirements before self-scan ([`fd6cc30`](https://github.com/sonatype-nexus-community/jake/commit/fd6cc30b34d56071a4c41d105646593cbc51719e))


## v0.2.53 (2020-11-12)

### Unknown

* 0.2.53

[skip ci] ([`e167375`](https://github.com/sonatype-nexus-community/jake/commit/e167375d896d5875d02f671d6460a2fc44828fac))

* Merge branch &#39;main&#39; of github.com:sonatype-nexus-community/jake into main ([`5ef66bb`](https://github.com/sonatype-nexus-community/jake/commit/5ef66bb975eb254ea002994c34d2ff264185b24f))

* internal build: don&#39;t scan semantic version release log for headers. invisible infrastructure ([`9011de2`](https://github.com/sonatype-nexus-community/jake/commit/9011de21c83c513addb2c2ddc7d344cd8db4d7bf))


## v0.2.52 (2020-11-12)

### Unknown

* 0.2.52

[skip ci] ([`286d9c7`](https://github.com/sonatype-nexus-community/jake/commit/286d9c7667b3147f8854d9147b7f1af38f299ea9))

* internal build: don&#39;t scan semantic version release log for headers. ([`aaab301`](https://github.com/sonatype-nexus-community/jake/commit/aaab301310f62130ee71158ce5676ca01c058567))


## v0.2.51 (2020-11-11)

### Unknown

* 0.2.51

[skip ci] ([`7f16d72`](https://github.com/sonatype-nexus-community/jake/commit/7f16d72b4ca7ace375baf7beeae44d5a724702d0))

* create separate &#39;development only&#39; requirements file (#40)

* create separate &#39;development only&#39; requirements file ([`7c1cd85`](https://github.com/sonatype-nexus-community/jake/commit/7c1cd8522c4df6473222c3f483469538fb84716f))


## v0.2.50 (2020-11-09)

### Unknown

* 0.2.50

[skip ci] ([`656b856`](https://github.com/sonatype-nexus-community/jake/commit/656b8565bb2e13814994d36e20de704d89126c16))

* remove extension parameter suffix from sbom &#39;version&#39; tag.  (#44)

* remove extension parameter suffix from sbom &#39;version&#39; tag. fixes #43 ([`8b6ddef`](https://github.com/sonatype-nexus-community/jake/commit/8b6ddef858c74ccb004c2371c17bc86945c33405))


## v0.2.49 (2020-09-25)

### Unknown

* 0.2.49

[skip ci] ([`86967b8`](https://github.com/sonatype-nexus-community/jake/commit/86967b8ca6a4aa27cad99c86afe25e0697bde0eb))

* switch semantic release to branch: main ([`26f215d`](https://github.com/sonatype-nexus-community/jake/commit/26f215d75185edbf1ac408eb534f268ca43657d1))

* switch internal build to branch: main ([`0a28d41`](https://github.com/sonatype-nexus-community/jake/commit/0a28d41da7ba3b04592d2d6cfa218deec5718a60))

* switch image reference to branch: main ([`3bfb57e`](https://github.com/sonatype-nexus-community/jake/commit/3bfb57ed88b3d77b6f470f2a46aebc9360e815a4))

* switch CircleCi release config to main ([`1694241`](https://github.com/sonatype-nexus-community/jake/commit/16942410ab135ac6b8898c856d77ba56719753ea))


## v0.2.48 (2020-09-22)

### Unknown

* 0.2.48

[skip ci] ([`921e271`](https://github.com/sonatype-nexus-community/jake/commit/921e2718cefba3b5dc084f7e009496cb6fdbda3a))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`88b4c68`](https://github.com/sonatype-nexus-community/jake/commit/88b4c688176d76000a256afa5c64655a489852c4))

* doh! stage-release ([`54f0d41`](https://github.com/sonatype-nexus-community/jake/commit/54f0d41ae1fe85d9fffc7a81f0397f3e80a3cfce))


## v0.2.47 (2020-09-22)

### Unknown

* 0.2.47

[skip ci] ([`ff317a7`](https://github.com/sonatype-nexus-community/jake/commit/ff317a74b5262b857978c65842c159c2b8ee7a08))

* scan at stage stage to trigger policy failures (instead of warnings). ([`a5e289e`](https://github.com/sonatype-nexus-community/jake/commit/a5e289ecf675df4cc6181a51849ce0024d1927ad))


## v0.2.46 (2020-09-22)

### Unknown

* 0.2.46

[skip ci] ([`43a8581`](https://github.com/sonatype-nexus-community/jake/commit/43a8581914c0f032ee984dbebdac631433629327))

* Handle IQ warning (#39)

* handle &#39;Warning&#39; from IQ policy ([`cdfd806`](https://github.com/sonatype-nexus-community/jake/commit/cdfd806a1151cde97747d6aa71577807ce1c4c15))


## v0.2.45 (2020-09-21)

### Unknown

* 0.2.45

[skip ci] ([`4a2d196`](https://github.com/sonatype-nexus-community/jake/commit/4a2d19639b63320a1fbcee6fc130d7f094855d1e))

* appease linter ([`2f61675`](https://github.com/sonatype-nexus-community/jake/commit/2f61675e3ab7adcc692258204f8d351c3a2e4fb9))

* let status code do its thang ([`ea76fed`](https://github.com/sonatype-nexus-community/jake/commit/ea76fed1e89b925759f6fa78eeab7c160dafea76))

* show response action value in message ([`7487d16`](https://github.com/sonatype-nexus-community/jake/commit/7487d1674aaba7bd40a112b9d3c62aaceaeed2de))

* try always cat log ([`210b7e3`](https://github.com/sonatype-nexus-community/jake/commit/210b7e3d82bcf9f68a33eade3b8aaeddadd2f86e))


## v0.2.44 (2020-09-21)

### Unknown

* 0.2.44

[skip ci] ([`a9029cc`](https://github.com/sonatype-nexus-community/jake/commit/a9029cc2a066da9f77ea8d942dfe578ea94e2fad))

* more shell madness ([`617d906`](https://github.com/sonatype-nexus-community/jake/commit/617d9066825b96300f98f1334aab5953ee62f828))


## v0.2.43 (2020-09-21)

### Unknown

* 0.2.43

[skip ci] ([`2bea418`](https://github.com/sonatype-nexus-community/jake/commit/2bea41812eb59beae8847204bf3a0bee93e4656f))

* fix fix failure detect ([`87df0dd`](https://github.com/sonatype-nexus-community/jake/commit/87df0dd5bc60e754e8e0d19c359b908e3d9a8f85))


## v0.2.42 (2020-09-21)

### Unknown

* 0.2.42

[skip ci] ([`753ae2f`](https://github.com/sonatype-nexus-community/jake/commit/753ae2f62c63d83edebe20f40f88a6b2a5b069d2))

* fix failure detect ([`8e60b05`](https://github.com/sonatype-nexus-community/jake/commit/8e60b05d824d819bbc59ca0c24e5ae811bb94dd8))


## v0.2.41 (2020-09-21)

### Unknown

* 0.2.41

[skip ci] ([`86603bb`](https://github.com/sonatype-nexus-community/jake/commit/86603bb1166e68dd665a0469424d653a867b55b3))

* cat log if failure occurs ([`595863d`](https://github.com/sonatype-nexus-community/jake/commit/595863dcfe3137169421e8bcf80baac0d0709d7c))


## v0.2.40 (2020-09-21)

### Unknown

* 0.2.40

[skip ci] ([`efa3fcf`](https://github.com/sonatype-nexus-community/jake/commit/efa3fcfe4d9d6e238fc9f7d88fc9575abf3ab858))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`99fb149`](https://github.com/sonatype-nexus-community/jake/commit/99fb149c591af3b2c6c3580b943df2fcddb2621c))

* typo madness ([`da77ee4`](https://github.com/sonatype-nexus-community/jake/commit/da77ee44e3d90b0b4c6be8f7bb70f215aa8139da))


## v0.2.39 (2020-09-21)

### Unknown

* 0.2.39

[skip ci] ([`e2adefd`](https://github.com/sonatype-nexus-community/jake/commit/e2adefd94fda43db0a86cbfe5ea427868dbab7bf))

* single quote path ([`312f05c`](https://github.com/sonatype-nexus-community/jake/commit/312f05caf0ad427242bfb70bfba4f07f92a79c45))


## v0.2.38 (2020-09-21)

### Unknown

* 0.2.38

[skip ci] ([`0f49e44`](https://github.com/sonatype-nexus-community/jake/commit/0f49e44152f710ba84de275f08351eaea1d44d19))

* double quote path ([`826f7a8`](https://github.com/sonatype-nexus-community/jake/commit/826f7a80f10bab2552f613f7db78cb437bf0b509))


## v0.2.37 (2020-09-21)

### Unknown

* 0.2.37

[skip ci] ([`849f2fd`](https://github.com/sonatype-nexus-community/jake/commit/849f2fd4a3a4a5136b80f8211d79fb0e21797bfb))

* print logfile location if verbose ([`64fd5ff`](https://github.com/sonatype-nexus-community/jake/commit/64fd5ff4f5f076beba912f0c8842ac358253b7d7))


## v0.2.36 (2020-09-21)

### Unknown

* 0.2.36

[skip ci] ([`66e9ac1`](https://github.com/sonatype-nexus-community/jake/commit/66e9ac13a67f5fb8bb28e4afa25dce2a6dd06bbb))

* another try at cat ([`b715113`](https://github.com/sonatype-nexus-community/jake/commit/b71511333a3e19c58d08a4da25548e989a9c7970))


## v0.2.35 (2020-09-21)

### Unknown

* 0.2.35

[skip ci] ([`59768d0`](https://github.com/sonatype-nexus-community/jake/commit/59768d0d20ebb24acf41fc8a2c5b5b1eb98c3bf8))

* skip copy for now ([`91deef2`](https://github.com/sonatype-nexus-community/jake/commit/91deef248b67f7a24c9cce40d1ef461232d9f8eb))


## v0.2.34 (2020-09-21)

### Unknown

* 0.2.34

[skip ci] ([`c705c73`](https://github.com/sonatype-nexus-community/jake/commit/c705c73d10c63755ae9ff3cd2be0862b99b5dc3f))

* archive will not work if run before the scan ([`144e51f`](https://github.com/sonatype-nexus-community/jake/commit/144e51f7619d86540db9ceceb0297aaa9babbc00))


## v0.2.33 (2020-09-21)

### Unknown

* 0.2.33

[skip ci] ([`01daa1a`](https://github.com/sonatype-nexus-community/jake/commit/01daa1af3005fac4bd262b8445ee3a36d9052722))

* try to capture log in Jenkins ([`b7fb9ca`](https://github.com/sonatype-nexus-community/jake/commit/b7fb9ca6245045bd38bcc1d5bea50b08a59df23f))


## v0.2.32 (2020-09-21)

### Unknown

* 0.2.32

[skip ci] ([`6652e2a`](https://github.com/sonatype-nexus-community/jake/commit/6652e2ae1e039b936c4d8d8bb7eaba9ff0dd955e))

* archive Jake log from Jenkins CI build, outside method call ([`624ef60`](https://github.com/sonatype-nexus-community/jake/commit/624ef60ea8cb087dc247ca851b742e6f1006c1aa))


## v0.2.31 (2020-09-21)

### Unknown

* 0.2.31

[skip ci] ([`f279d1e`](https://github.com/sonatype-nexus-community/jake/commit/f279d1ecb167895611f40aa87b573e6a210e4be4))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`06cf758`](https://github.com/sonatype-nexus-community/jake/commit/06cf7589e8cc414da49d9d725386f3c81440570d))

* archive Jake log from Jenkins CI build ([`43703fb`](https://github.com/sonatype-nexus-community/jake/commit/43703fb59854ada6c48d7e7aee90612a345efef2))

* err msg typo ([`3fa5744`](https://github.com/sonatype-nexus-community/jake/commit/3fa5744b9534b2fb3e820bdc217f34107153ed79))


## v0.2.30 (2020-09-21)

### Unknown

* 0.2.30

[skip ci] ([`16b1258`](https://github.com/sonatype-nexus-community/jake/commit/16b12581068c85712c3be7b0ed30a0519aeeff6e))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`7017f6a`](https://github.com/sonatype-nexus-community/jake/commit/7017f6a09f0e99f56358451c38ac964a686f648f))

* increase verbosity of Jenkins build ([`024eb3a`](https://github.com/sonatype-nexus-community/jake/commit/024eb3a614e49f5e448a2901941b713be791120a))


## v0.2.29 (2020-09-21)

### Unknown

* 0.2.29

[skip ci] ([`0b1127f`](https://github.com/sonatype-nexus-community/jake/commit/0b1127f2ada12f2fe0676cdfb53cf2dab7d66a80))

* add `responses` testing dependency to Jenkinsfile ([`3272ea9`](https://github.com/sonatype-nexus-community/jake/commit/3272ea92be6b44dae31d101a8cbbb0bc22eabb8b))


## v0.2.28 (2020-09-18)

### Unknown

* 0.2.28

[skip ci] ([`69defb7`](https://github.com/sonatype-nexus-community/jake/commit/69defb75052539682e44473d8566b327f6a3403d))

* Unit tests for IQ (#38)

💥 ([`2b52a19`](https://github.com/sonatype-nexus-community/jake/commit/2b52a194b91ee3d452bd7156c443c69a2a4730fe))


## v0.2.27 (2020-09-11)

### Unknown

* 0.2.27

[skip ci] ([`834e8a0`](https://github.com/sonatype-nexus-community/jake/commit/834e8a07d2d7a9ca47bdb46ba7ffa497b6c050d2))

* Add failure notification to internal CI ([`ea1e3bd`](https://github.com/sonatype-nexus-community/jake/commit/ea1e3bdc43924bd1f9ebe17f87e1d5e400f37527))


## v0.2.26 (2020-09-10)

### Unknown

* 0.2.26

[skip ci] ([`0af0e1a`](https://github.com/sonatype-nexus-community/jake/commit/0af0e1a42a643d37e1fb084ed21ec43921b130d8))

* Allow insecure requests (#35)

* Allow insecure for IQ ([`0775797`](https://github.com/sonatype-nexus-community/jake/commit/07757975b0f00222da97fb6a408684d11d0b0b11))


## v0.2.25 (2020-09-03)

### Unknown

* 0.2.25

[skip ci] ([`03a7037`](https://github.com/sonatype-nexus-community/jake/commit/03a7037a382625ca3ac12c853fec39fb4f975039))

* Drop six as a dependency (#33)

* Drop stuff that includes six

* Drop line length

* Whitespace and line length

* Errant print

* removed six as a direct dep

* removed six as a direct dep

Co-authored-by: glenn &lt;Glenn Mohre&gt; ([`ef053a8`](https://github.com/sonatype-nexus-community/jake/commit/ef053a8cc6b9deaa9e7fd16275b01bf30582f82a))


## v0.2.24 (2020-06-05)

### Unknown

* 0.2.24

[skip ci] ([`a1dd340`](https://github.com/sonatype-nexus-community/jake/commit/a1dd3401c8f3faac41dad8a836c2b3d9e7f4098d))

* Group good &#39;n&#39; bad vulnerabilities and output them in tables (#30)

Co-authored-by: Jeffry Hesse &lt;5544326+DarthHater@users.noreply.github.com&gt;
Co-authored-by: michelkazi &lt;michel.m.kazi@gmail.com&gt; ([`2de93b4`](https://github.com/sonatype-nexus-community/jake/commit/2de93b4e5c3c80db623104b34f3450fd4ff703ad))


## v0.2.23 (2020-05-29)

### Unknown

* 0.2.23

[skip ci] ([`89513a2`](https://github.com/sonatype-nexus-community/jake/commit/89513a2b5c0da0b1121a913973b61c41c6df52e2))

* Password ([`33fdcd1`](https://github.com/sonatype-nexus-community/jake/commit/33fdcd1f445f69ac5dfea25f9ebe576666bef719))

* Welp ([`55138ee`](https://github.com/sonatype-nexus-community/jake/commit/55138eeb4e8b2a3270ff742584f8b44a8206210d))

* Flip the script ([`38f8a08`](https://github.com/sonatype-nexus-community/jake/commit/38f8a08f23d60d0c0aefe948dae5520dab0ad8a1))


## v0.2.22 (2020-05-29)

### Unknown

* 0.2.22

[skip ci] ([`7600809`](https://github.com/sonatype-nexus-community/jake/commit/7600809f15c57a5dc486f8c7a36058d80afdd0a1))

* Ok ([`ec0cce2`](https://github.com/sonatype-nexus-community/jake/commit/ec0cce255d3358416aacea83bd18907617f20ced))


## v0.2.21 (2020-05-29)

### Unknown

* 0.2.21

[skip ci] ([`3c2713e`](https://github.com/sonatype-nexus-community/jake/commit/3c2713e77177583cae4ddfe9450e88ced0d6e459))

* One more try ([`6a4dbe1`](https://github.com/sonatype-nexus-community/jake/commit/6a4dbe12104315f05c7a818ee361e9fee70cc7a1))


## v0.2.20 (2020-05-29)

### Unknown

* 0.2.20

[skip ci] ([`395a007`](https://github.com/sonatype-nexus-community/jake/commit/395a00789ef1da50fab619c06cef12dcc90f079f))

* ENV not run ([`97d1acf`](https://github.com/sonatype-nexus-community/jake/commit/97d1acf13990a0523e47ffffba7e42887ba16eea))


## v0.2.19 (2020-05-29)

### Unknown

* 0.2.19

[skip ci] ([`f956b58`](https://github.com/sonatype-nexus-community/jake/commit/f956b588da3e59749ee8d6b94002736f905024f7))

* Path with local bin ([`8a505cb`](https://github.com/sonatype-nexus-community/jake/commit/8a505cbcb334b2b77234d68461b5f9b2a8b6ac81))


## v0.2.18 (2020-05-29)

### Unknown

* 0.2.18

[skip ci] ([`d43a067`](https://github.com/sonatype-nexus-community/jake/commit/d43a067b1b8d01db59196d38cf257c0950c9ec5c))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`af4f461`](https://github.com/sonatype-nexus-community/jake/commit/af4f46178f6a9968db5288d7698c346011c9625e))

* Lil diff useradd ([`7b9481a`](https://github.com/sonatype-nexus-community/jake/commit/7b9481ae01e0d2f1ee051c84079e38be9668ae37))


## v0.2.17 (2020-05-29)

### Unknown

* 0.2.17

[skip ci] ([`bf08469`](https://github.com/sonatype-nexus-community/jake/commit/bf08469470993b2709d2bb86565406bf984513f2))

* More Jenkins ([`7192f73`](https://github.com/sonatype-nexus-community/jake/commit/7192f739f20504ab77cbbf5c187422d5cb0f39d4))


## v0.2.16 (2020-05-29)

### Unknown

* 0.2.16

[skip ci] ([`06c7767`](https://github.com/sonatype-nexus-community/jake/commit/06c7767fe968a9f3fe15b3fc8852185e336a120f))

* Copy in requirements ([`8311eab`](https://github.com/sonatype-nexus-community/jake/commit/8311eab10187d5269dba107dea759fcee3b4310d))

* Simplify this down a tad ([`ba551aa`](https://github.com/sonatype-nexus-community/jake/commit/ba551aadeb1b178256e462a4b4b5773a25079f09))


## v0.2.15 (2020-05-28)

### Unknown

* 0.2.15

[skip ci] ([`7b7f2ac`](https://github.com/sonatype-nexus-community/jake/commit/7b7f2ac253be0f2eecb022115d67b66444e563cd))

* Skip alpine due to missing gcc ([`58a1460`](https://github.com/sonatype-nexus-community/jake/commit/58a146021b8bd8a177c6a63b7f3594f36109957a))


## v0.2.14 (2020-05-28)

### Unknown

* 0.2.14

[skip ci] ([`bb751e1`](https://github.com/sonatype-nexus-community/jake/commit/bb751e1abb480c6108329457580fd495e5731470))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`bf0b831`](https://github.com/sonatype-nexus-community/jake/commit/bf0b83138821ef8f652236c768f7057df4524ebf))

* Docker and then run tests ([`f512a94`](https://github.com/sonatype-nexus-community/jake/commit/f512a94a74272b5e8d83249de1352775b1fb9abf))


## v0.2.13 (2020-05-28)

### Unknown

* 0.2.13

[skip ci] ([`3fb506b`](https://github.com/sonatype-nexus-community/jake/commit/3fb506b53f6f9dd0f2ffcd80f73ed2199f9aefb1))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`ba819f5`](https://github.com/sonatype-nexus-community/jake/commit/ba819f551cec894dd3189dd5af45e909bd70d1c0))

* Run them scripts ([`90634ec`](https://github.com/sonatype-nexus-community/jake/commit/90634ec021b9248337969eed5332638f6a77f684))


## v0.2.12 (2020-05-28)

### Unknown

* 0.2.12

[skip ci] ([`302184e`](https://github.com/sonatype-nexus-community/jake/commit/302184e1362e0e1500115ffe3c04ef7b576b5579))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`fcf0d48`](https://github.com/sonatype-nexus-community/jake/commit/fcf0d488ad9d2cb527606ecb7cd25dc319d71e65))

* Plz ([`d3ef5d7`](https://github.com/sonatype-nexus-community/jake/commit/d3ef5d7484f7518b89ecc0fe90476aa006165a77))


## v0.2.11 (2020-05-28)

### Unknown

* 0.2.11

[skip ci] ([`8b0d70e`](https://github.com/sonatype-nexus-community/jake/commit/8b0d70e183362b7639d8e864555bde19e621dd02))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`fb5836a`](https://github.com/sonatype-nexus-community/jake/commit/fb5836a5b5e190c4e95901b7ec08a29af4eb6c0a))

* HEADAHZ ([`6c1160d`](https://github.com/sonatype-nexus-community/jake/commit/6c1160de7273d2957ed2ed5be5a3f9c287c48385))


## v0.2.10 (2020-05-28)

### Unknown

* 0.2.10

[skip ci] ([`3545e3c`](https://github.com/sonatype-nexus-community/jake/commit/3545e3c07e47573ab60b9012ce5726aab0db3af6))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`54db0f2`](https://github.com/sonatype-nexus-community/jake/commit/54db0f2bb7d2aa143a5cc3f5f4d6d36473b757d2))

* Come on headers ([`0326db4`](https://github.com/sonatype-nexus-community/jake/commit/0326db4c8aaace965e2a94938f02560c11966dc0))


## v0.2.9 (2020-05-28)

### Unknown

* 0.2.9

[skip ci] ([`1a8fcfd`](https://github.com/sonatype-nexus-community/jake/commit/1a8fcfdbfb68babfd229414320caf64f1f761059))

* Merge master ([`32fa5e6`](https://github.com/sonatype-nexus-community/jake/commit/32fa5e61500d48c87d80bca846164618db69c27b))

* More headers ([`29d91a4`](https://github.com/sonatype-nexus-community/jake/commit/29d91a4b45d0a8c582ccec3269ee546c71d632ef))


## v0.2.8 (2020-05-28)

### Unknown

* 0.2.8

[skip ci] ([`ce60314`](https://github.com/sonatype-nexus-community/jake/commit/ce60314b37c9c9e4e5389733b33021e45a0489a0))

* Ok try this header out ([`8ddd6ad`](https://github.com/sonatype-nexus-community/jake/commit/8ddd6adb2465710a438a536510c1a7d131e27670))


## v0.2.7 (2020-05-28)

### Unknown

* 0.2.7

[skip ci] ([`f13456f`](https://github.com/sonatype-nexus-community/jake/commit/f13456fbb7bac084a85748c717208a4cd7641252))

* Another header adjust ([`1b4447f`](https://github.com/sonatype-nexus-community/jake/commit/1b4447fb3ffb5d79a3305c9ddb42cf59efebec35))

* Adjust this header ([`47019da`](https://github.com/sonatype-nexus-community/jake/commit/47019da3f32de5d6eb627a8fa51937ebd8be51d8))


## v0.2.6 (2020-05-28)

### Unknown

* 0.2.6

[skip ci] ([`8d70958`](https://github.com/sonatype-nexus-community/jake/commit/8d70958a07d5a5468b08c02aa38c6fa8b90c840f))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`8897017`](https://github.com/sonatype-nexus-community/jake/commit/889701775b0d5d3a751a6bf02e6d538bc1c4992d))

* Change header, setup excludes ([`3df0940`](https://github.com/sonatype-nexus-community/jake/commit/3df09408305fbb9356d4af431cbe0c989ce8a3fb))


## v0.2.5 (2020-05-28)

### Unknown

* 0.2.5

[skip ci] ([`9bc23dd`](https://github.com/sonatype-nexus-community/jake/commit/9bc23ddbc57617c07f4c31d6d5c9167c3aafb502))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`0c199df`](https://github.com/sonatype-nexus-community/jake/commit/0c199df495d9a57fb6e11d9e39653f1704c637e4))

* Initial header ([`44214f5`](https://github.com/sonatype-nexus-community/jake/commit/44214f57e1d684078912e841989fa92c9cd1d137))


## v0.2.4 (2020-05-28)

### Unknown

* 0.2.4

[skip ci] ([`82205f2`](https://github.com/sonatype-nexus-community/jake/commit/82205f20c971e270d45c06db33ae05c83da1690e))

* Jenkins and Dockerfile ([`f18bfad`](https://github.com/sonatype-nexus-community/jake/commit/f18bfada520af60e22a15bdedfa66d2792a246da))


## v0.2.3 (2020-05-21)

### Unknown

* 0.2.3

[skip ci] ([`f4f2150`](https://github.com/sonatype-nexus-community/jake/commit/f4f21501595800e882829220b3e3ab2eaef2e40c))

* New jake logo ([`8e08148`](https://github.com/sonatype-nexus-community/jake/commit/8e08148119e8a31e46e70350f3e9c28dd29100b6))


## v0.2.2 (2020-05-20)

### Unknown

* 0.2.2

[skip ci] ([`322d367`](https://github.com/sonatype-nexus-community/jake/commit/322d367e6f49db5d0e8d9324a559c0d56f22a0e8))

* Update README to mention support ([`1044d28`](https://github.com/sonatype-nexus-community/jake/commit/1044d289926843fe267a6d2dfee0f1f026c335bb))


## v0.2.1 (2020-05-12)

### Unknown

* 0.2.1

[skip ci] ([`3669fae`](https://github.com/sonatype-nexus-community/jake/commit/3669fae6bde3edc126486ff4bc6ce2c6ba0fc5a9))

* simplified IQ service and handled authentication errors with the command line ([`d1331e5`](https://github.com/sonatype-nexus-community/jake/commit/d1331e55eaffa8f3d385cde8c3af3e05c8469eff))

* [skip ci] reset semver to patch ([`6dd4454`](https://github.com/sonatype-nexus-community/jake/commit/6dd4454dfd04e0b7a18039b46d04e1f7b46a259f))


## v0.2.0 (2020-05-12)

### Unknown

* 0.2.0

[skip ci] ([`429dfa0`](https://github.com/sonatype-nexus-community/jake/commit/429dfa0155c6861321a0af2cc38a0c750be8fd29))

* Sbom mkdir if it doesn&#39;t exist and error handling (#24)

Fixes #23 and #25 

Releases a major version

* added line to create the directory specified in the output file if it doesn&#39;t exist

* added error handling for some directory making conditions

* removed random logger assignment i did.  Should we be printing error messages through the logger or...?

* added support for windows OS

* publishing a minor release with these fixes since we added the sbom export recently

Co-authored-by: Ben Foltz &lt;ben.h.foltz@gmail.com&gt; ([`a68ef01`](https://github.com/sonatype-nexus-community/jake/commit/a68ef01e0ea5ec242060c8bd76bb6f2205b2076f))


## v0.1.7 (2020-05-01)

### Unknown

* 0.1.7

[skip ci] ([`6288fb2`](https://github.com/sonatype-nexus-community/jake/commit/6288fb22fc93b194bdd287986b27a8e87f709e58))

* modified sbom subcommand to output to std_out by default, and to a file with the -o &lt;file&gt; arg.  Also implemented an std_out toggle and made the -q flag suppress all unnecessary output for each subcommand ([`f833717`](https://github.com/sonatype-nexus-community/jake/commit/f833717d8df90448d39bc4018aa5256dd9947b75))


## v0.1.6 (2020-04-30)

### Unknown

* 0.1.6

[skip ci] ([`f90dcda`](https://github.com/sonatype-nexus-community/jake/commit/f90dcda5dcb12327e9bfe95ea3539574ffe123b6))

* hotfix to make the sbom output command work with the new targets argument ([`a737043`](https://github.com/sonatype-nexus-community/jake/commit/a737043c1673e8d11dbdb4f3adbbbb3ab08a7db1))


## v0.1.5 (2020-04-30)

### Unknown

* 0.1.5

[skip ci] ([`4b25da5`](https://github.com/sonatype-nexus-community/jake/commit/4b25da5cfbcd18b2d3fb09bccb04b361e2b61c50))

* Decoupled IQ from OSSI, output cyclonedx sbom to file, added arg to scan site/dist package directories (#22)

* updated dependencies

* added some return types and handled empty list on get internal id response

* fixed tests

* actually fixed linter failures

* changed all the module imports to be relative

* moved the conda flag into shared opts and the clear cache flag to an eager callback

* suppressed non-vulnerable oss index output with the quiet param

* error handling for conda flag when there is no stdin

* BAM! IQ is decoupled from ossi completely.  Just added a function to the generator class to take in a list of purls to generate the xml from

* fixed spinners and tests

* changed IQ messages for final result output

* added subcommand to output the cyclonedx sbom to a file on the system

* clean up, name changes, comments

* more cleanup

* added some return types

* figured it out, can export the site-packages into a variable and then pass it in as a command line target.  Now the --target param will allow you to evaluate any site package including those in virtual environment.  Will update readme with instructions

* updated readme and fixed the argument names

* more readme stuff and fixed the pylint warnings

* hehehehehe...

* more readme changes ([`5b0a595`](https://github.com/sonatype-nexus-community/jake/commit/5b0a595628268241c43f8bb153adbdd4744f30f8))


## v0.1.4 (2020-04-24)

### Unknown

* 0.1.4

[skip ci] ([`86ab80c`](https://github.com/sonatype-nexus-community/jake/commit/86ab80c0ef19b44a5efe43a6a742752eca08bb95))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`fdb3a80`](https://github.com/sonatype-nexus-community/jake/commit/fdb3a80e55fcd0692f472a4a66a1f4b7a3ef4749))

* Ok xsd files ([`f1c1c09`](https://github.com/sonatype-nexus-community/jake/commit/f1c1c0962cec73eca730b50dcb3aa00c0cfb350d))


## v0.1.3 (2020-04-24)

### Unknown

* 0.1.3

[skip ci] ([`a659251`](https://github.com/sonatype-nexus-community/jake/commit/a659251e79a5f8c108ee2362a1c4d06a95b6e576))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`a848a74`](https://github.com/sonatype-nexus-community/jake/commit/a848a74d983a19e793a989d6a0d5506f77e8ebc9))

* Include xsd files ([`4016127`](https://github.com/sonatype-nexus-community/jake/commit/40161273ea051cd4805a2452fe97148786add481))


## v0.1.2 (2020-04-23)

### Unknown

* 0.1.2

[skip ci] ([`cddc7b7`](https://github.com/sonatype-nexus-community/jake/commit/cddc7b7cb2524982aa9c10e6c9ffb4607f7c5d19))

* Artie is a nice person but do not delete __init__.py plz ([`f617d2d`](https://github.com/sonatype-nexus-community/jake/commit/f617d2d6eb7089d7e07dd70a8f79df3ea83ee593))


## v0.1.1 (2020-04-23)

### Unknown

* 0.1.1

[skip ci] ([`2acbadb`](https://github.com/sonatype-nexus-community/jake/commit/2acbadbc66caafe7d58b032fd326c8a5ea40c478))

* Add this back in ([`3bcaf10`](https://github.com/sonatype-nexus-community/jake/commit/3bcaf1058a6bebcff33bfc698ea2af10305f43dc))

* [skip ci] reset to patch ([`735a6f2`](https://github.com/sonatype-nexus-community/jake/commit/735a6f2e75d0d7886bd5b5dadac07e02a3e9ff51))


## v0.1.0 (2020-04-23)

### Unknown

* 0.1.0

[skip ci] ([`b852d7f`](https://github.com/sonatype-nexus-community/jake/commit/b852d7f5e75a6f4c0767b6e27a878c593d2228ef))

* Follow a tip from my buddy @bhamail, use a shell script, and setup a venv, etc..., and see if this works without sudo ([`ad603ab`](https://github.com/sonatype-nexus-community/jake/commit/ad603aba744a385c1b7314294457d727cb0ffedd))

* PIP IN JAKE (#21)

* PIP IN JAKE

* Get away from urllib3 1.25.6

* HYBRIDIZED RESULTS FOR CONDA BABY

* pulled some logic related to constructing purls into the Coordinates object to allow for easier combines between sets of coordinates

* added changed to conda parsing to use new Coordinates type

* more conversions and added a join function to Coordinates.  For a conda iq scan it is currently overlaying both results with no deduping.  Should be easy to prune the joined dict to remove any dupes

* commented out the stuff for the hybridized conda results, cleaned up formatting and added comments

* Added stage specification for the IQ scan

* fixed unit tests that broke when Coordinate was refactored

* fixed all the import statements that pylint was screaming about by removing the init file in the same directory as the main entrypoint

* changed the pip parser to generate the dependency list as coordinates on init and added a getter function to fix the pylint error

* modified pylint to ignore two trvial cases failing the build

* fixed the disables, vals don&#39;t need quotes or semicolons

* disabling warnings because they are failing the circle-ci build

* added scaffolding for an argparser with subcommands that directly calls functions in the class.  haven&#39;t wired it up yet

* refactored command line and argument parsing to include subparsers

* removed some code and fixed some issues

* added some comments, readability

* docstring for a thing

* changed a couple things to pass tests

* changed the config so that if non-none params are passed in for auth or IQ endpoint it gets it from confog.  still have to figure out the best place to inject default config params, probably if a file config does not exist

* added the host and auth params for iq to the command line and routed them to the IQ request service.  it now checks if a config exists on the IQ request service side, and if it does, use that unless there are command line params.  If it doesn&#39;t, user the default params unless there are command line params.  Logger doesn&#39;t go into the IQ service for some reason, gotta figure that one out.

* made it so its just passing the args namespace from argparse down all the way to the iq request service so its only one variable.  Still not sure how logs are working, should figure out how to make it unified across all classes and set the level in the command line.

* some comments, removed a line or two

* initial pass at tearing out argparse and putting in click, working out well so far.  It also has the potential to clean up the code significantly

* threw in the rest of the arguments, just need to consolidate the rest of the logic into the functions that run under each subcommand

* removing old argparse code

* all wired up and good to go for ddt conda/pypi and IQ pypi.  completely messed up the logging output, although it looks like click can output various messages to the console.  No need to have a logger if click can log as well no?

* WOOOOOOOOHHHEEEEEEE we got ourselves a banging wiring job now

* some linting fixes.  Not sure what to do about the iq function names as it map to the sub-command in click.  or does it?  will add docstrings later

* one last thing, just had to add a BOMB-ASS BANNERgit add *!

* alright not to scoop honey out my own pot but this is looking righteous AF

* added some comments and fixed the version prompt never working by making it hit a callback that exits the script

* Ternaries and clean up

* 2 spaces

* UGH

* Improve jake ddt --help

* Disable pylint for arguments and name

* more comments, got rid of linter errors this one should pass

* mas

* Share them args

* Output that ding ol version

* YA SPIN YA, plus color

* removed line that pip freeze throws onto requirements.txt, i&#39;ve been manually updating since there aren&#39;t that many deps anyway

* Some more improvements to outputting results

* fixed

* Fix

* Setup logger

* LOGGER

* Logging level

* Commands and banner

* Logger

* MAX SCORE

* Fix pylint or disable

* some readme and help text changes

* more readme changes

* small fixes to readme and adjusting circleci config to do a minor release rather than a path for merge to master

Co-authored-by: ButterB0wl &lt;ajurgenson@sonatype.com&gt; ([`28cc553`](https://github.com/sonatype-nexus-community/jake/commit/28cc553b384a690e676f2fabd324698214449a18))


## v0.0.21 (2020-01-11)

### Unknown

* 0.0.21

[skip ci] ([`f5df45d`](https://github.com/sonatype-nexus-community/jake/commit/f5df45d4b24d609dddb03a5c67bdb02e27082527))

* refactor to use explicit validate_xml_vulnerabilities() method (#18) ([`abf2d18`](https://github.com/sonatype-nexus-community/jake/commit/abf2d186e8c727315600d5935046be4c393e386d))


## v0.0.20 (2020-01-08)

### Unknown

* 0.0.20

[skip ci] ([`5c1580b`](https://github.com/sonatype-nexus-community/jake/commit/5c1580bfac482987f7154c2c2da37fe1c90fe621))

* add &#39;Nexus IQ Server&#39; example to doco ([`70c133b`](https://github.com/sonatype-nexus-community/jake/commit/70c133b92cf19657435f53c46a0a1b5db36e0a62))


## v0.0.19 (2020-01-08)

### Unknown

* 0.0.19

[skip ci] ([`5114dcc`](https://github.com/sonatype-nexus-community/jake/commit/5114dcc08a6f5bd71174ad2a60c8c1b74cbf8fe5))

* Yaml for Config (#16)

💥 ([`689b765`](https://github.com/sonatype-nexus-community/jake/commit/689b76561500d7e84a1ec0925fbb5b25a13ee4a3))


## v0.0.18 (2020-01-06)

### Unknown

* 0.0.18

[skip ci] ([`1752d59`](https://github.com/sonatype-nexus-community/jake/commit/1752d596768086ead2499a49d3d4499a150e58ef))

* minor message typo ([`9834788`](https://github.com/sonatype-nexus-community/jake/commit/983478811627c97c09bff7e6c21ce036f4090163))


## v0.0.17 (2020-01-03)

### Unknown

* 0.0.17

[skip ci] ([`c1a015e`](https://github.com/sonatype-nexus-community/jake/commit/c1a015e6ccdc9ff836755f16c66cf3469885a2bc))

* Make Jake work with IQ Server (#15)

💥 

Co-authored-by: Allen Hsieh &lt;10136383+allenhsieh@users.noreply.github.com&gt; ([`e6f7a63`](https://github.com/sonatype-nexus-community/jake/commit/e6f7a639d7b01872dbc2667871530f491e7557b8))


## v0.0.16 (2019-11-13)

### Unknown

* 0.0.16

[skip ci] ([`69fc132`](https://github.com/sonatype-nexus-community/jake/commit/69fc132afce707611147b47a6f751c28c963eb50))

* add some test results to CI (#14)

* add some test results to CI ([`e0f5949`](https://github.com/sonatype-nexus-community/jake/commit/e0f5949636c7eb932887b084a8938bd3f6fa3076))


## v0.0.15 (2019-11-11)

### Unknown

* 0.0.15

[skip ci] ([`71ed6dc`](https://github.com/sonatype-nexus-community/jake/commit/71ed6dcf6c5559246eb0317bc46f7ad3f5a1b61a))

* remove unused cache commands (&#34;Pipfile.lock&#34; didn&#39;t even exists, so all cache commands errored out). ([`476666d`](https://github.com/sonatype-nexus-community/jake/commit/476666d94481baed003f5ac1f321dc07cd8892b3))


## v0.0.14 (2019-11-08)

### Unknown

* 0.0.14

[skip ci] ([`66b3e6f`](https://github.com/sonatype-nexus-community/jake/commit/66b3e6fbfd45c7908bf053d6e0ee142d09f9138a))

* Make CI scripts fail on any error (#13) ([`de9485f`](https://github.com/sonatype-nexus-community/jake/commit/de9485f01055a0daac8955c11caa8d7b09363e04))


## v0.0.13 (2019-11-06)

### Unknown

* 0.0.13

[skip ci] ([`2fa6454`](https://github.com/sonatype-nexus-community/jake/commit/2fa64547c9afe1ec24699de5b07f98a896d1b4ce))

* cleaning up ([`8a6130d`](https://github.com/sonatype-nexus-community/jake/commit/8a6130de87be31a4a25ea8de008d35a2fb9c40c5))


## v0.0.12 (2019-11-06)

### Unknown

* 0.0.12

[skip ci] ([`73c4baa`](https://github.com/sonatype-nexus-community/jake/commit/73c4baa7615cd8ebd6ead8eee598de680c674cbb))

* Give it a twirl ([`3a3031f`](https://github.com/sonatype-nexus-community/jake/commit/3a3031ff81c8af4c0634e0ce91f77921b41e6fa2))

* attempting to publish with new permissions ([`99f438f`](https://github.com/sonatype-nexus-community/jake/commit/99f438f86a2559c24288ed3d332e6d2be894a755))

* 0.0.11

[skip ci] ([`d5df7e1`](https://github.com/sonatype-nexus-community/jake/commit/d5df7e17b9789118613a243072dbf61e65075cb9))

* attempting to fix logger ([`2e60c3d`](https://github.com/sonatype-nexus-community/jake/commit/2e60c3d0d6fd28c05d3c1a900af68814f1ee5e63))


## v0.0.10 (2019-11-06)

### Unknown

* 0.0.10

[skip ci] ([`8f5b48a`](https://github.com/sonatype-nexus-community/jake/commit/8f5b48aa7ebab8ed32ae531480802a320d35642a))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`f2b23d0`](https://github.com/sonatype-nexus-community/jake/commit/f2b23d02b76ebb40d1e81eafa5fd56bd288378cb))

* Welp ([`7bce551`](https://github.com/sonatype-nexus-community/jake/commit/7bce5516684fa65933967cbfd5f771c1b12925a3))


## v0.0.9 (2019-11-06)

### Unknown

* 0.0.9

[skip ci] ([`5a0afed`](https://github.com/sonatype-nexus-community/jake/commit/5a0afed45cba822320cad2afa6578448993cb52d))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`5a98a6b`](https://github.com/sonatype-nexus-community/jake/commit/5a98a6baaa9b3dd6ec11dc52a379dd4a66868593))

* Find packages again ([`391e7bc`](https://github.com/sonatype-nexus-community/jake/commit/391e7bc40723609839b707c932b7bc4c51f191a0))


## v0.0.8 (2019-11-06)

### Unknown

* 0.0.8

[skip ci] ([`cf46555`](https://github.com/sonatype-nexus-community/jake/commit/cf4655517c205880e958237c382c69f8a3fde67d))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`17b931c`](https://github.com/sonatype-nexus-community/jake/commit/17b931c2060ead91497efd477e4f496db37900ca))

* Find packages ([`e9c4ed2`](https://github.com/sonatype-nexus-community/jake/commit/e9c4ed2efe0f3f9d3628192f0ec33496e452c68b))


## v0.0.7 (2019-11-06)

### Unknown

* 0.0.7

[skip ci] ([`fabd311`](https://github.com/sonatype-nexus-community/jake/commit/fabd3115f599e5c040d1a31633fabe2663decf61))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`b69125a`](https://github.com/sonatype-nexus-community/jake/commit/b69125ae3ccf3143cbe752349af9bf6788d242f3))

* More explicit import ([`362f7df`](https://github.com/sonatype-nexus-community/jake/commit/362f7dfce045f7531e2fd9ff3174815b6d20f422))


## v0.0.6 (2019-11-06)

### Unknown

* 0.0.6

[skip ci] ([`d8fe9fd`](https://github.com/sonatype-nexus-community/jake/commit/d8fe9fd61acfde45bd44fcc388439c2c832ed5aa))

* what ([`59a4827`](https://github.com/sonatype-nexus-community/jake/commit/59a482746c3290ee1ac22f25cfa4781bcf894506))

* Pip3 ([`961ba24`](https://github.com/sonatype-nexus-community/jake/commit/961ba24f37b54651919bd10da18b4c43001cee21))

* Ok ([`37eee44`](https://github.com/sonatype-nexus-community/jake/commit/37eee44fa174699763354bb4ecf677e9d7c33e12))

* Oh come on ([`07aaf72`](https://github.com/sonatype-nexus-community/jake/commit/07aaf728fb2168970f4bb070534062a78d92aa4c))

* REALLY ([`edac8df`](https://github.com/sonatype-nexus-community/jake/commit/edac8dff061f21f10db09a672821f711c9bdcebc))

* JAKE ([`67dc40b`](https://github.com/sonatype-nexus-community/jake/commit/67dc40b81a3cdf3171bac8066cc70358b6599b30))

* removed python-semantic-release ([`d6ce302`](https://github.com/sonatype-nexus-community/jake/commit/d6ce30221350a6c651e98092e9997b1c67b22674))

* remove pickledb ([`8ccbaeb`](https://github.com/sonatype-nexus-community/jake/commit/8ccbaeb38423f8512102cebeeb8925f37a2a9e88))

* attempting verbose logging ([`09f6102`](https://github.com/sonatype-nexus-community/jake/commit/09f61026b05c07903f196662c70b7a63590d49ea))


## v0.0.5 (2019-11-05)

### Unknown

* 0.0.5

[skip ci] ([`a7b8bbe`](https://github.com/sonatype-nexus-community/jake/commit/a7b8bbea17c130080b8490575684e45634d0d971))

* Okie ([`ef0c424`](https://github.com/sonatype-nexus-community/jake/commit/ef0c42452ab67a4d080d103211df71fd1bf0f466))


## v0.0.4 (2019-11-05)

### Unknown

* 0.0.4

[skip ci] ([`0b76c43`](https://github.com/sonatype-nexus-community/jake/commit/0b76c43e05c554023081b61a0097318432a2eacb))

* Upgrade setuptools ([`3fe5d14`](https://github.com/sonatype-nexus-community/jake/commit/3fe5d14af9f0569cb5a082bedaaeda819f38133b))


## v0.0.3 (2019-11-05)

### Unknown

* 0.0.3

[skip ci] ([`e882d2f`](https://github.com/sonatype-nexus-community/jake/commit/e882d2f41d43d98fc46746cef971741a1a9a2433))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`67d0e61`](https://github.com/sonatype-nexus-community/jake/commit/67d0e61f857420a12786df790799836ca5f3a585))

* Description ([`9a0e3ac`](https://github.com/sonatype-nexus-community/jake/commit/9a0e3ac53b053fed4f95a77896d63e891d6481a0))


## v0.0.2 (2019-11-05)

### Unknown

* 0.0.2

[skip ci] ([`dfc81da`](https://github.com/sonatype-nexus-community/jake/commit/dfc81da38b53fdbf008b88891af29358288cca67))

* Updates ([`ebf80e4`](https://github.com/sonatype-nexus-community/jake/commit/ebf80e47e5742a30bd9cf87be9923a65dcf15732))


## v0.0.1 (2019-11-05)

### Unknown

* 0.0.1

[skip ci] ([`ca95475`](https://github.com/sonatype-nexus-community/jake/commit/ca95475aa6e012b5c5a5602d98a2d3bad116c923))

* Ok with gusto ([`da9150c`](https://github.com/sonatype-nexus-community/jake/commit/da9150c79fbc49372dd4b8c66ed4ac7d29342bb8))

* 0.0.1

[skip ci] ([`3fe0e5e`](https://github.com/sonatype-nexus-community/jake/commit/3fe0e5ee439192eabac1e8f239691a2217f8a972))

* Ok ([`5714c0e`](https://github.com/sonatype-nexus-community/jake/commit/5714c0e8db4847621fbf5c9633f269ff86090641))

* YOLO ([`72ea6a1`](https://github.com/sonatype-nexus-community/jake/commit/72ea6a126ffc7a015e9379dfab21193712b04555))

* 0.0.2

[skip ci] ([`2f34d02`](https://github.com/sonatype-nexus-community/jake/commit/2f34d025dc59d9d1a0dc7e8f7039950c6abc0632))

* remove obsolete ssh key voodoo ([`8aa6a46`](https://github.com/sonatype-nexus-community/jake/commit/8aa6a46a99f3600172a182ec134d72b8ef81f88e))

* 0.0.1

[skip ci] ([`32cb9bf`](https://github.com/sonatype-nexus-community/jake/commit/32cb9bfc44b9d9c5b455f6a81eb32020d84d2f78))

* To PyPI we go ([`2468c1b`](https://github.com/sonatype-nexus-community/jake/commit/2468c1b5068d6994da7be01d04b4b244d2150267))

* 0.0.5

[skip ci] ([`4c1da65`](https://github.com/sonatype-nexus-community/jake/commit/4c1da6504ef21d7b2e4c5a97d920b98e09ae6450))

* Extra YOLO ([`377f64a`](https://github.com/sonatype-nexus-community/jake/commit/377f64a9a838b5f2e11e72cb300aedb4cfebe1f8))

* 0.0.4

[skip-ci] ([`fcec96e`](https://github.com/sonatype-nexus-community/jake/commit/fcec96e85dd2e1a2b7d1cc7c677b63db8843b4ef))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`33d0aa9`](https://github.com/sonatype-nexus-community/jake/commit/33d0aa96db6ef2fd28317c3ea935a531cd223341))

* Extra yolo ([`04b6f47`](https://github.com/sonatype-nexus-community/jake/commit/04b6f4798be79fb9d32be349d7f301b898a8ab32))

* YOLO ([`d3daa1a`](https://github.com/sonatype-nexus-community/jake/commit/d3daa1ab46737018e2d9dc6cf4e246ff4da970b4))

* 0.0.3

&#34;[skip-ci]&#34; ([`aca79e3`](https://github.com/sonatype-nexus-community/jake/commit/aca79e3d9df78e9ad59d15d76a90dba836391669))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`248b962`](https://github.com/sonatype-nexus-community/jake/commit/248b9624e4da100f1b28485b3744981eb83ca5ba))

* Skip ci for commit message ([`1e75251`](https://github.com/sonatype-nexus-community/jake/commit/1e75251f6f15ea256cd7824d9cc8c7c62a8b73a1))

* Merge branch &#39;master&#39; of github.com:sonatype-nexus-community/jake ([`c2a81c7`](https://github.com/sonatype-nexus-community/jake/commit/c2a81c7ad4175a1aeb5668df4ecd92380500bb3d))

* ssh funness ([`12a79ac`](https://github.com/sonatype-nexus-community/jake/commit/12a79aca23ee034233bb6f1028bec09e6380b489))

* Extra YOLO ([`1d1495b`](https://github.com/sonatype-nexus-community/jake/commit/1d1495bb69575a208e17a44e109d2af0ea964e8f))

* YOLO ([`065bd14`](https://github.com/sonatype-nexus-community/jake/commit/065bd14e9d79dfd9fb6181fc5e46f616671bdadb))

* Semantic release (#12)

Semantic Release fun stuff ([`005d0c6`](https://github.com/sonatype-nexus-community/jake/commit/005d0c67e44e03be5ee30d50be81d56f7f1ed35a))


## v0.0.0 (2019-11-06)

### Unknown

* Added the ability to use OSSIndex account to prevent rate limiting (#10)

💥 ([`b15ac01`](https://github.com/sonatype-nexus-community/jake/commit/b15ac01fe05bb99b2896b92d174f4561df80c1a6))

* fix typo in pip install command. link back to build instructions (hopefully). ([`34f49a7`](https://github.com/sonatype-nexus-community/jake/commit/34f49a70bf0fc5971fefd60a1c92e0336db6537d))

* Move ([`6ddc21a`](https://github.com/sonatype-nexus-community/jake/commit/6ddc21afb639bf911a87fbfd589bfa95a41fea9b))

* More templates ([`f3a82f8`](https://github.com/sonatype-nexus-community/jake/commit/f3a82f81e6e007d132577d3987b763f1f89a1c43))

* Update issue templates ([`235d042`](https://github.com/sonatype-nexus-community/jake/commit/235d04225528fa548b86c011ab2ca3d3e6e00309))

* Implemented caching in jake  (#7)

* Implemented caching in jake ([`a5a31cc`](https://github.com/sonatype-nexus-community/jake/commit/a5a31ccff490f9e5ed022665d193c8d4e747929d))

* Chunking requests and fixing tests (#5)

* Chunking requests to OSSIndex and fixing tests ([`7cdf0f5`](https://github.com/sonatype-nexus-community/jake/commit/7cdf0f547eda9fecc34f579d276bdfae5170268c))

* Allow jake to use stdin (#4)

* changed to using stdin instead of run_command ([`de2c2c9`](https://github.com/sonatype-nexus-community/jake/commit/de2c2c9bc51c51657d1885aedcbbcf949e5e3de7))

* we need badges - ci badge - fixes #2 ([`e25ccae`](https://github.com/sonatype-nexus-community/jake/commit/e25ccae97f2c733f507de51bf54a06c9eb796bbc))

* happy pep ([`b3f9155`](https://github.com/sonatype-nexus-community/jake/commit/b3f915585cf7c0eac8f2ea9c6e7397b84468e08e))

* minor cleanup ([`6573616`](https://github.com/sonatype-nexus-community/jake/commit/65736166e789117d67ae7629ab5c500361c6eb95))

* yolo - tests, weeee ([`54dba6b`](https://github.com/sonatype-nexus-community/jake/commit/54dba6bc15ec45c745b22c81fa346736e542e906))

* refactor to use argparse ([`cf0242b`](https://github.com/sonatype-nexus-community/jake/commit/cf0242b16ab15cc7b250abfcc3ea8c5f34a5aaba))

* handle empty list ([`4f2204f`](https://github.com/sonatype-nexus-community/jake/commit/4f2204f8745b774626a3d1ae6bab7fd093b98d81))

* Ok more progress ([`d19db5c`](https://github.com/sonatype-nexus-community/jake/commit/d19db5c3bf54f8fa8a8964f76d780629822244bc))

* Initial WIP ([`c25d15b`](https://github.com/sonatype-nexus-community/jake/commit/c25d15be2eacff9fffe5995aefb87923fa6be0ae))
