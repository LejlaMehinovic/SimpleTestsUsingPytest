import pytest
import requests
from requests import get
import json


def test_valid():
    url = "https://reqres.in/api/login/"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    t = json.loads(response.text)
    assert response.status_code == 200
    assert t["token"] == "QpwL5tke4Pnpja7X4"
