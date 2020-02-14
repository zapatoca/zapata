#!/usr/bin/env python3

import time

pytest_plugins = ["docker_compose"]


def test_title(selenium, function_scoped_container_getter):
    time.sleep(5)
    selenium.get('http://localhost:8200')
    assert selenium.title == 'Vault'
