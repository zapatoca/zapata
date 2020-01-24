#!/usr/bin/env python3

import pytest

from zapata import create_app
from zapata.routes import configure_routes


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def app():
    app = create_app()
    configure_routes(app)
    return app
