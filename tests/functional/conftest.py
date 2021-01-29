import os
import time

import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    if os.getenv("GITHUB_ACTIONS"):
        guest_home = os.getenv("GITHUB_WORKSPACE")
    else:
        guest_home = "/Users/liora/repos/github.com/lioramilbaum/zapata"
    monkeypatch.setenv("GUEST_HOME", guest_home)


@pytest.fixture
def init_db():
    if os.getenv("GITHUB_ACTIONS"):
        time.sleep(30)
        os.system(
            "docker exec -t db psql -U zapata -d zapata -f /tmp/dump.sql"
        )
