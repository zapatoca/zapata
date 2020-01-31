#!/usr/bin/env bash


apt-get update
apt-get install -y mysql-server

systemctl enable mysql
systemctl start mysql
