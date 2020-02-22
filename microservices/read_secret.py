#!/usr/bin/env python3

import json

import requests


def main():
    with open('/vagrant/microservices/vault/vaultkeys', 'r') as vaultkeys:
        f = json.loads(vaultkeys.read())
        token = f['root_token']
        keys = f['keys']
    headers = {"X-Vault-Token": "{0}".format(token)}
    response = requests.get(url='http://localhost:8200/v1/sys/seal-status')
    if json.loads(response.content)['sealed']:
        response = requests.put(
            url='http://localhost:8200/v1/sys/unseal',
            data='{{"key": "{key}"}}'.format(key=keys[0])
        )
    response = requests.get(
        url='http://localhost:8200/v1/kv/data/secret/mysql/password',
        headers=headers
    )
    print(json.loads(response.content)['data']['data']['key'])


if __name__ == "__main__":
    main()
