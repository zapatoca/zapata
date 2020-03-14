#!/usr/bin/env python3

from flask import Flask
from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)
    return app


def create_db(app):
    app.config['MYSQL_HOST'] = '127.0.0.1'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'zapata'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.secret_key = 'secret123'

    db = MySQL(app)
    return db
