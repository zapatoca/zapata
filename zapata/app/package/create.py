#!/usr/bin/env python3

from flask import Flask
from flask_mysqldb import MySQL


def create_app():
    app = Flask(
        __name__,
        template_folder='/app/templates',
        static_folder='/app/static'
    )
    return app


def create_db(app):
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'zapata'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    app.secret_key = 'secret123'

    db = MySQL(app)
    return db
