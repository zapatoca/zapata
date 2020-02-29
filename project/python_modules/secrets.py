#!/usr/bin/env python3

import json
import os

import requests


def get_secret(key):
    if os.getenv("GUEST_HOME") is not None:
        vaultkeysfile = os.getenv('GUEST_HOME') + \
            '/microservices/vault/vaultkeys'
    else:
        vaultkeysfile = '/microservices/vault/vaultkeys'
    with open(vaultkeysfile, 'r') as vaultkeys:
        f = json.loads(vaultkeys.read())
        token = f['root_token']
        keys = f['keys']
    response = requests.get(url='http://localhost:8200/v1/sys/seal-status')
    if json.loads(response.content)['sealed']:
        response = requests.put(
            url='http://localhost:8200/v1/sys/unseal',
            data='{{"key": "{key}"}}'.format(key=keys[0])
        )
    headers = {"X-Vault-Token": "{0}".format(token)}
    response = requests.get(
        url='http://localhost:8200/v1/kv/data/secret/{key}'.format(key=key),
        headers=headers
    )
    return json.loads(response.content)['data']['data']['key']
