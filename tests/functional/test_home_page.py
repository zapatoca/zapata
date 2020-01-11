#!/usr/bin/env python3


def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
