import pytest
import json
from main import app

def test_get_all():
    response = app.test_client().get('http://localhost:5000/products')
    assert response.status_code == 200
    if response.status_code == 200:
        result = json.loads(response.json)
        assert isinstance(result, list)


