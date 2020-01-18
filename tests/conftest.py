#!/usr/bin/env python3

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from zapata import create_app
from zapata.routes import configure_routes


@pytest.fixture()
def test_client():
    app = create_app()
    configure_routes(app)
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options
