#!/usr/bin/env python3


def test_selenium(selenium):
    selenium.get('http://localhost:5000')
    assert selenium.title == 'Zapata'
