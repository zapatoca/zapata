#!/usr/bin/env python3

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
