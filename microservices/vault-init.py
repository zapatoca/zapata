#!/usr/bin/env python3

import json
import os

import hvac
from dotenv import load_dotenv


def get_keys():
    with open('/vault/vaultkeys', 'r') as vaultkeys:
        return json.load(vaultkeys)['keys']


def get_token():
    with open('/vault/vaultkeys', 'r') as vaultkeys:
        return json.load(vaultkeys)['root_token']


def main():
    load_dotenv(dotenv_path='/.env')
    client = hvac.Client(url='http://vault:8200')
    if os.path.exists("/vault/vaultkeys"):
        os.remove("/vault/vaultkeys")
    with open('/vault/vaultkeys', 'w') as vaultkeys:
        json.dump(client.sys.initialize(1, 1), vaultkeys)
    if client.sys.is_sealed():
        client.sys.submit_unseal_keys(get_keys())
    client.token = get_token()

    client.sys.enable_secrets_engine(
        backend_type='kv',
        path='kv',
        options=dict(version=2),
    )
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/mysql/password',
        secret=dict(key=os.getenv('MYSQL_PASSWORD')),
        mount_point='kv'
    )
    os.system('chown -R 1000:0 /vault')


if __name__ == "__main__":
    main()
