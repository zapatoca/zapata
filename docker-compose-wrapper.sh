#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

apt-get update
apt-get install -y python3-pip

pip3 install -r $GUEST_HOME/requirements.txt

MYSQL_ROOT_PASSWORD=$(cd $GUEST_HOME && export GUEST_HOME=$GUEST_HOME && python3 -c "from modules.secrets import get_secret; print(get_secret('localhost', 'mysql/password'))")
export MYSQL_ROOT_PASSWORD
docker-compose -f $GUEST_HOME/docker-compose.yml up --build -d db app