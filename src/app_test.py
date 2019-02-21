"""Tests for the Flask API in `app.py`."""
from flask import url_for
import pytest

from app import api


@pytest.fixture
def app():
    """Fixture representing the app context for our Flask API."""
    return api


def test_api_parse_ingredient(client):
    """Happy path test: A parseable json request, returns a parsed json response."""
    res = client.post(url_for('ingredient'), json=({'ing': '500.5 grams of salt'}))
    assert res.json == {
        "ingredient": "salt",
        "quantity": "500.5",
        "unit": "g"
    }
