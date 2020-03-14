#!/usr/bin/env python3

import os

import MySQLdb
import pytest

from modules.secrets import get_secret


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def mysql():
    print(get_secret('localhost', 'mysql/password'))
    return MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd=get_secret('localhost', 'mysql/password')
    )


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    if os.getenv("GITHUB_ACTIONS"):
        guest_home = os.getenv("GITHUB_WORKSPACE")
    else:
        guest_home = '/Users/liora/src/github.com/lioramilbaum/zapata'
    monkeypatch.setenv('GUEST_HOME', guest_home)
