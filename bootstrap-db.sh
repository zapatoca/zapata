#!/usr/bin/env bash

GUEST_HOME=${GUEST_HOME:='.'}

sleep 30
MYSQL_PASSWORD=$(cd /vagrant && python3 -c "from project.python_modules.secrets import get_secret; print(get_secret('mysql/password'))")
debconf-set-selections <<< "mysql-server mysql-server/root_password password $MYSQL_PASSWORD"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $MYSQL_PASSWORD"

apt-get update
apt-get install -y mysql-server libmysqlclient-dev

systemctl enable mysql
systemctl start mysql

echo -e "\n[mysqld]\nbind-address = 0.0.0.0" >> /etc/mysql/my.cnf
systemctl restart mysql

mysql -u root -proot -e "CREATE DATABASE zapata;"
mysql -u root -proot zapata < $GUEST_HOME/create_db.sql
