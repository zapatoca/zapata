#!/usr/bin/env python3


def test_title(selenium, init_db):
    selenium.get("http://localhost:5000")
    assert selenium.title == "Zapata"


def test_logo_click(selenium):
    selenium.get("http://localhost:5000")
    selenium.find_element_by_class_name("navbar-brand").click()
    assert selenium.current_url == "http://localhost:5000/"


def test_tables(selenium):
    selenium.get("http://localhost:5000/")
    tables = selenium.find_elements_by_tag_name("table")
    assert len(tables) == 2
