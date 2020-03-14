#!/usr/bin/env python3

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_title(selenium):
    selenium.get('http://localhost:8200')
    assert selenium.title == 'Vault'


def test_vault_initialized(selenium):
    selenium.get('http://localhost:8200')
    try:
        WebDriverWait(selenium, 10).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title is-3"), "Unseal Vault"
            )
        )
    except Exception:
        return False
