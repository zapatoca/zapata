#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

apt-get update
apt-get install -y python3-pip python3-setuptools mysql-client libmysqlclient-dev

pip3 install -r $GUEST_HOME/requirements.lock

MYSQL_ROOT_PASSWORD=$(cd $GUEST_HOME && export GUEST_HOME=$GUEST_HOME && python3 -c "from project.secrets import get_secret; print(get_secret('mysql/password'))")
export MYSQL_ROOT_PASSWORD
docker-compose -f $GUEST_HOME/microservices/docker-compose.yml up -d db