#!/usr/bin/env python3

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

pytest_plugins = ["docker_compose"]


def test_title(selenium, session_scoped_container_getter):
    selenium.get('http://localhost:8200')
    assert selenium.title == 'Vault'


def test_vault_initialized(selenium, session_scoped_container_getter):
    selenium.get('http://localhost:8200')
    try:
        WebDriverWait(selenium, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title is-3"), "Unseal Vault"
            )
        )
    except Exception:
        return False
