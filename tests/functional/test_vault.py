#!/usr/bin/env python3

pytest_plugins = ["docker_compose"]


def test_title(selenium, function_scoped_container_getter):
    selenium.get('http://localhost:8200')
    assert selenium.title == 'Vault'
