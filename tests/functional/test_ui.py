#!/usr/bin/env python3

import time

import pytest
from selenium.webdriver.support.color import Color


def test_title(selenium):
    selenium.get("http://localhost:5000")
    assert selenium.title == "Zapata"


def test_logo_click(selenium):
    selenium.get("http://localhost:5000")
    selenium.find_element_by_class_name("navbar-brand").click()
    assert selenium.current_url == "http://localhost:5000/home"


def test_header(selenium):
    selenium.get("http://localhost:5000")
    selenium.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    element1 = selenium.find_element_by_class_name("background-header")
    element2 = selenium.find_element_by_class_name(
        "navbar-brand"
    ).find_element_by_tag_name("h2")
    element3 = selenium.find_element_by_class_name(
        "navbar-brand"
    ).find_element_by_tag_name("h3")
    assert (
        element1.value_of_css_property("background-color")
        == "rgb(255, 255, 255)"
    )
    assert element2.value_of_css_property("color") == "rgb(30, 30, 30)"
    assert element3.value_of_css_property("color") == "rgb(30, 30, 30)"


@pytest.mark.parametrize("test_input", [("kuku@stam.com")])
def test_new_subscriber(selenium, test_input):
    selenium.get("http://localhost:5000")
    selenium.find_element_by_id("email").send_keys(test_input)
    selenium.find_element_by_class_name("main-button").click()
    assert selenium.current_url == "http://localhost:5000/home"
    assert selenium.find_element_by_id("email").get_attribute("value") == ""


def test_building(selenium):
    selenium.get("http://localhost:5000/building")
    cols = selenium.find_elements_by_xpath("//table/thead/tr[1]/th")
    assert len(cols) == 3
    rows = selenium.find_elements_by_xpath("//table/tbody/tr")
    assert len(rows) == 19
    table = selenium.find_element_by_tag_name("table")
    assert (
        table.value_of_css_property("background-color")
        == Color.from_string("white").rgb
    )
