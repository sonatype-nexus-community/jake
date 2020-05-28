#
# Copyright (c) 2019-present Sonatype, Inc. All rights reserved.
# Includes the third-party code listed at http://links.sonatype.com/products/clm/attributions.
# "Sonatype" is a trademark of Sonatype, Inc.
#

FROM docker-all.repo.sonatype.com/python:3.7-alpine

COPY requirements.txt ./

COPY .circleci/ci-run.sh ./

COPY .circleci/ci-setup.sh ./
