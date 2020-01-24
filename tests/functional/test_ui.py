#!/usr/bin/env python3

import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
class TestLiveServer():

    def test_server_is_up_and_running(self, selenium):
        selenium.get(url_for('home', _external=True))
        assert selenium.title == 'Zapata'
