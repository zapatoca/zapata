#!/usr/bin/env python3

import json
import os
import time

import requests


def get_secret(host, key):
    endpoint = "http://%s:%s" % (host, '8200')
    while True:
        status_code = requests.get(endpoint + '/v1/sys/health').status_code
        if status_code == 200:
            break
        time.sleep(5)
    if os.getenv("GUEST_HOME") is not None:
        vaultkeysfile = os.getenv('GUEST_HOME') + \
            '/zapata/vault/vaultkeys'
    else:
        vaultkeysfile = '/vault/vaultkeys'
    with open(vaultkeysfile, 'r') as vaultkeys:
        f = json.loads(vaultkeys.read())
        token = f['root_token']
        keys = f['keys']
    response = requests.get(url=endpoint+'/v1/sys/seal-status')
    if json.loads(response.content)['sealed']:
        response = requests.put(
            url=endpoint+'/v1/sys/unseal',
            data='{{"key": "{key}"}}'.format(key=keys[0])
        )
    headers = {"X-Vault-Token": "{0}".format(token)}
    response = requests.get(
        url=endpoint+'/v1/kv/data/secret/{key}'.format(key=key),
        headers=headers
    )
    return json.loads(response.content)['data']['data']['key']
