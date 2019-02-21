from flask import url_for
import pytest

from app import api


@pytest.fixture
def app():
    return api


def test_api_parse_ingredient(client):
    res = client.post(url_for('ingredient'), json=({'ing': '500.5 grams of salt'}))
    assert res.json == {
        "ingredient": "salt",
        "quantity": "500.5",
        "unit": "g"
    }