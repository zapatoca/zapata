#!/usr/bin/env bash


apt-get update
apt-get install -y python3-pip

pip3 install -r /vagrant/requirements.lock

chmod 755 /vagrant/zapata/app.py
nohup python3 /vagrant/zapata/app.py > /dev/null 2>&1 &
