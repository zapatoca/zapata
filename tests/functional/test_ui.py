#!/usr/bin/env python3

import time

import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
class TestLiveServer():

    @pytest.mark.parametrize('page', [
        'home'
    ])
    def test_title(self, selenium, page):
        selenium.get(url_for(page, _external=True))
        assert selenium.title == 'Zapata'

    @pytest.mark.parametrize('page', [
        'home'
    ])
    def test_logo_click(self, selenium, page):
        selenium.get(url_for(page, _external=True))
        selenium.find_element_by_class_name('navbar-brand').click()
        assert selenium.current_url == url_for(page, _external=True)

    @pytest.mark.parametrize('page', [
        'home'
    ])
    def test_header(self, selenium, page):
        selenium.get(url_for(page, _external=True))
        selenium.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        element1 = selenium.find_element_by_class_name("background-header")
        element2 = selenium.find_element_by_class_name(
            "navbar-brand").find_element_by_tag_name("h2")
        element3 = selenium.find_element_by_class_name(
            "navbar-brand").find_element_by_tag_name("h3")
        assert element1.value_of_css_property(
            "background-color") == "rgb(255, 255, 255)"
        assert element2.value_of_css_property(
            "color") == "rgb(30, 30, 30)"
        assert element3.value_of_css_property(
            "color") == "rgb(30, 30, 30)"

    @pytest.mark.parametrize('test_input', [
        ('kuku@stam.com')
    ])
    def test_new_subscriber(self, selenium, test_input):
        selenium.get(url_for('home', _external=True))
        selenium.find_element_by_id('email').send_keys(test_input)
        selenium.find_element_by_class_name('main-button').click()
        assert selenium.current_url == url_for('home', _external=True)
        assert selenium.find_element_by_id(
            'email').get_attribute('value') == ""
