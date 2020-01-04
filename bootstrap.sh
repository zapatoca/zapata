#!/usr/bin/env bash


apt-get update
apt-get install -y python3-pip

pip3 install -r /vagrant/requirements.lock

chmod 755 /vagrant/main.py

export FLASK_APP=/vagrant/main.py
nohup python3 -m flask run --host=0.0.0.0 > /dev/null 2>&1 &
