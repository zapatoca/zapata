#!/usr/bin/env python3


def test_title(selenium):
    selenium.get("http://localhost:5000")
    assert selenium.title == "Zapata"


def test_logo_click(selenium):
    selenium.get("http://localhost:5000")
    selenium.find_element_by_class_name("navbar-brand").click()
    assert selenium.current_url == "http://localhost:5000/"


def test_table(selenium):
    selenium.get("http://localhost:5000/")
    cols = selenium.find_elements_by_xpath("//table/thead/tr[1]/th")
    assert len(cols) == 5
    rows = selenium.find_elements_by_xpath("//table/tbody/tr")
    assert len(rows) == 19
