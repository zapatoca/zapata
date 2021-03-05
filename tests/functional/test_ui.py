#!/usr/bin/env python3


def test_title(selenium):
    selenium.get("https://localhost:8443")
    assert selenium.title == "Zapata"


def test_logo_click(selenium):
    selenium.get("https://localhost:8443")
    selenium.find_element_by_class_name("navbar-brand").click()
    assert selenium.current_url == "https://localhost:8443/"


def test_tables(selenium):
    selenium.get("https://localhost:8443/")
    tables = selenium.find_elements_by_tag_name("table")
    assert len(tables) == 4


def test_navbar(selenium):
    selenium.get("https://localhost:8443/")
    assert selenium.current_url == "https://localhost:8443/"
    selenium.find_element_by_link_text("Home").click()
    assert selenium.current_url == "https://localhost:8443/"
    selenium.find_element_by_link_text("Projects").click()
    assert selenium.current_url == "https://localhost:8443/projects"
    selenium.find_element_by_link_text("New Project").click()
    assert selenium.current_url == "https://localhost:8443/projects/new"
    selenium.find_element_by_link_text("Fees").click()
    assert selenium.current_url == "https://localhost:8443/fees"
    selenium.find_element_by_link_text("New Fee").click()
    assert selenium.current_url == "https://localhost:8443/fees/new"
