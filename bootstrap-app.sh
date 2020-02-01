#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

apt-get update
apt-get install -y python3-pip

pip3 install -r /vagrant/requirements.lock

chmod 755 /vagrant/main.py

export FLASK_APP=$GUEST_HOME/main.py
nohup python3 -m flask run --host=0.0.0.0 > /dev/null 2>&1 &
