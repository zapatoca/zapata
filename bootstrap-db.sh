#!/usr/bin/env bash

debconf-set-selections <<< 'mysql-server mysql-server/root_password password 12345'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 12345'

apt-get update
apt-get install -y mysql-server

systemctl enable mysql
systemctl start mysql

mysql -u root -p12345 -e "CREATE DATABASE zapata;"
mysql -u root -p12345 zapata < /vagrant/create_db.sql
