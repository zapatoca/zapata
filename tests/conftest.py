#!/usr/bin/env python3

import pytest

from project import create_app, create_db
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
