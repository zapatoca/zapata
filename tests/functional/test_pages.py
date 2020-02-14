#!/usr/bin/env python3

import pytest


@pytest.mark.parametrize('page', [
    '/',
    '/home'
])
def test_page(client, page):
    response = client.get(page)
    assert response.status_code == 200
    assert b'<h2>Zapata</h2>' in response.data
