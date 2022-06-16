#!/usr/bin/env bash
set -e
set -o pipefail
set -u

#Run the python publish script
python3 python/publish.py
