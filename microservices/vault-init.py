#!/usr/bin/env python3

import json
import os
import time

import hvac
import requests
from dotenv import load_dotenv


def get_keys():
    with open('/vault/vaultkeys', 'r') as vaultkeys:
        return json.load(vaultkeys)['keys']


def get_token():
    with open('/vault/vaultkeys', 'r') as vaultkeys:
        return json.load(vaultkeys)['root_token']


def import_secrets(client):
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/mysql/password',
        secret=dict(key=os.getenv('MYSQL_PASSWORD')),
        mount_point='kv'
    )
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/mailchimp/username',
        secret=dict(key=os.getenv('MAILCHIMP_USERNAME')),
        mount_point='kv'
    )
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/mailchimp/apikey',
        secret=dict(key=os.getenv('MAILCHIMP_APIKEY')),
        mount_point='kv'
    )
    client.secrets.kv.v2.create_or_update_secret(
        path='secret/mailchimp/listid',
        secret=dict(key=os.getenv('MAILCHIMP_LISTID')),
        mount_point='kv'
    )


def main():
    load_dotenv(dotenv_path='/.env')
    while (requests.get(url='http://vault:8200').status_code != 200):
        time.sleep(10)
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
    import_secrets(client)
    os.system('chown -R 1000:0 /vault')


if __name__ == "__main__":
    main()
