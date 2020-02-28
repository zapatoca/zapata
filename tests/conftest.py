#!/usr/bin/env python3

import MySQLdb
import pytest

from project import create_app, create_db
from project.python_modules.secrets import get_secret
from project.routes import configure_routes


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def app():
    app = create_app()
    db = create_db(app)
    configure_routes(app, db)
    return app


@pytest.fixture
def mysql():
    return MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd=get_secret('mysql/password')
    )
