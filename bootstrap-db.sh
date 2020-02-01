#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'

apt-get update
apt-get install -y mysql-server libmysqlclient-dev

systemctl enable mysql
systemctl start mysql

echo -e "\n[mysqld]\nbind-address = 0.0.0.0" >> /etc/mysql/my.cnf
systemctl restart mysql

mysql -u root -proot -e "CREATE DATABASE zapata;"
mysql -u root -proot zapata < $GUEST_HOME/create_db.sql
