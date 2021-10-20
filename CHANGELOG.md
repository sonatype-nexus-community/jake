# Changelog

<!--next-version-placeholder-->

## v1.0.1 (2021-10-20)
### Fix
* Update to support returning non-zero exit code when issues found (will return 1) ([`7667bac`](https://github.com/sonatype-nexus-community/jake/commit/7667bacb171803f7963bec12240520985103d06c))

## v1.0.0 (2021-10-18)
### Feature
* Sonatype Nexus IQ Lifecycle analysis is now migrated to using cyclonedx-python-lib ([`214d182`](https://github.com/sonatype-nexus-community/jake/commit/214d1821fa94ff895a2bfa4eac0f6961df093f46))
* Support Poetry for gleaning packages within the current environment to generate an SBOM ([`b9a1e5d`](https://github.com/sonatype-nexus-community/jake/commit/b9a1e5d2f38963a033d102399827c5c4dfe786da))
* Jake's OSS calls now utilising ossindex-lib and cyclonedx-python-lib ([`ec83583`](https://github.com/sonatype-nexus-community/jake/commit/ec83583520aa5ff8180b215b55846ed7a6fd487c))

### Fix
* Additional whitespace removed ([`709f7a2`](https://github.com/sonatype-nexus-community/jake/commit/709f7a2aa752668daba99c04b36ad9b8a6d271f2))
* Runtime tweaks to make it more robust ([`13c9028`](https://github.com/sonatype-nexus-community/jake/commit/13c902838008377e11e4c47ed619401776b8f782))
* Typos noted as updating documentation ([`0d65116`](https://github.com/sonatype-nexus-community/jake/commit/0d65116a17757b1ccf4c73bc463ee677eef0d5ff))

### Breaking
* `jake` has been re-written in large part to consume two new external libraries: - `cyclonedx-python-lib` which gives `jake` ability to more easily consume your depenedencies in a variety of manners (environment, Pipfile.lock, poetry.lock, requirements.txt) and support output in both JSON and XML at different schema versions - `ossindex-lib`: most of the functionallity for talking to OSS Index that was in `jake` has been externalised to this library to allow others to consume it ([`e11cb20`](https://github.com/sonatype-nexus-community/jake/commit/e11cb208c215169d6ce24fa8898a5aa2402d8791))

## v0.2.77 (2021-07-06)
### Fix
* CVE-2021-33503 in urllib3 == 1.26.4 ([#62](https://github.com/sonatype-nexus-community/jake/issues/62)) ([`9dfbb1c`](https://github.com/sonatype-nexus-community/jake/commit/9dfbb1c18831a1456803299e2f98a95ba95ea2b8))

## v0.2.76 (2021-06-29)
### Fix
* "ModuleNotFoundError: No module named 'typing_extensions'", occurring in 'python3.7/site-packages/tinydb/queries.py", line 28' on Jenkins CI ([#61](https://github.com/sonatype-nexus-community/jake/issues/61)) ([`a747750`](https://github.com/sonatype-nexus-community/jake/commit/a7477505a0e6d1b198461a75ef8d755cc37dfe12))

## v0.2.75 (2021-05-25)


## v0.2.74 (2021-05-25)


## v0.2.73 (2021-05-25)


## v0.2.72 (2021-05-13)
### Fix
* Inline targets help changes ([#58](https://github.com/sonatype-nexus-community/jake/issues/58)) ([`c146a7d`](https://github.com/sonatype-nexus-community/jake/commit/c146a7d87e0859040b01278de8a2d09eb9b8b1cb))

## v0.2.71 (2021-05-13)
### Fix
* #49 allow newer version of dependencies ([#57](https://github.com/sonatype-nexus-community/jake/issues/57)) ([`15553d4`](https://github.com/sonatype-nexus-community/jake/commit/15553d43932feca9978931734cf70c655158417d))

## v0.2.70 (2021-04-07)
### Fix
* CVE-2020-14343 in PyYAML==5.3.1 ([`11dc3c9`](https://github.com/sonatype-nexus-community/jake/commit/11dc3c90a2df876e2cda02be33a38c5f2a0c3fc4))

## v0.2.69 (2021-03-25)
### Fix
* CVE-2021-28957 in lxml==4.6.2 ([`6d4373c`](https://github.com/sonatype-nexus-community/jake/commit/6d4373cd8fe320a17d3f8ca95208a0d5b38888ee))

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
### Fix
* Resolve vulnerability: CVE-2020-27783 in lxml ([`7526728`](https://github.com/sonatype-nexus-community/jake/commit/7526728623e102fb75fad30eb82be8824abbdf39))

## v0.2.58 (2020-12-07)


## v0.2.57 (2020-11-12)


## v0.2.56 (2020-11-12)


## v0.2.55 (2020-11-12)


## v0.2.54 (2020-11-12)


## v0.2.53 (2020-11-12)


## v0.2.52 (2020-11-12)


## v0.2.51 (2020-11-11)


## v0.2.50 (2020-11-09)

