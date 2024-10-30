GitHub Actions Notes
====================

Local Builds
---------------
See: [Running GitHub Actions Locally](https://contribute.sonatype.com/docs/how-to/testing-github-actions-locally/).

In my case, on a Mac, I had to add the `-self-hosted` argument:
```shell
act -j build-and-test -P macos-latest=-self-hosted
```
