#!/usr/bin/env python3

import os

import MySQLdb
import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def mysql():
    return MySQLdb.connect(host="127.0.0.1", user="root", passwd="root")


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    if os.getenv("GITHUB_ACTIONS"):
        guest_home = os.getenv("GITHUB_WORKSPACE")
    else:
        guest_home = "/Users/liora/src/github.com/lioramilbaum/zapata"
    monkeypatch.setenv("GUEST_HOME", guest_home)
