#!/usr/bin/env sh

set -x

apk add jq
vault operator init --format json | jq '.' | cat > /vault/vaultkeys
chown -R 1000:0 /vault/vaultkeys
