#!/usr/bin/env sh

set -x

apk add --no-cache jq python3
python3 -m ensurepip
rm -r /usr/lib/python*/ensurepip
pip3 install --no-cache --upgrade pip setuptools wheel
pip3 install --no-cache -r /requirements.lock
/usr/local/bin/vault-init.py