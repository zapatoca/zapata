#!/usr/bin/env python3

import pytest


@pytest.mark.parametrize('page', [
    '/',
    '/home',
    '/contact',
    '/about',
    '/services'
])
def test_page(test_client, page):
    response = test_client.get(page)
    assert response.status_code == 200
    assert b'<title>Zapata</title>' in response.data
    assert b'<h2>Zapata</h2>' in response.data
