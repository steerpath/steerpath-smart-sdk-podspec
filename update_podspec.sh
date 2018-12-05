#!/usr/bin/env bash
set -e
set -o pipefail
set -u

#iOS version and filename
IOS_SDK_VERSION=$(< smart-sdk-version.txt)

#Commit and tag release version
git add -A && git commit -m "Release ${IOS_SDK_VERSION}"
git tag ${IOS_SDK_VERSION}
