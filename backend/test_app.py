import pytest
import json
from app import app
from sample_data import sample_data

@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    return app.test_client()

def test_post(client):
    json_data = json.loads(sample_data.valid_post)
    response = client.post('http://localhost:5000/products',json=json_data)
    assert response.status_code == 201
    
def test_post_invalid_data_format(client):
    json_data = json.loads(sample_data.invalid_post)
    response = client.post('http://localhost:5000/products',json=json_data)
    assert response.status_code == 400
    if response.status_code == 400:
        assert response.json == {"error":"Invalid data format"}

def test_get_all(client):
    response = client.get('http://localhost:5000/products')
    assert response.status_code == 200
    if response.status_code == 200:
        result = json.loads(response.json)
        assert isinstance(result, list)
        
def test_get(client):
    assemblies = client.get('http://localhost:5000/products')
    assembly = json.loads(assemblies.json)
    assembly_id = assembly[0]["_id"]["$oid"]
    response = client.get('http://localhost:5000/product/'+ assembly_id)
    assert response.status_code == 200
    
def test_get_invalid_id(client):
    response = client.get('http://localhost:5000/product/invalid_id')
    assert response.status_code == 404
    
def test_put(client):
    assemblies = client.get('http://localhost:5000/products')
    assembly = json.loads(assemblies.json)
    assembly_id = assembly[0]["_id"]["$oid"]
    json_data = json.loads(sample_data.modified_valid_post)
    response = client.put('http://localhost:5000/product/'+ assembly_id, json=json_data)
    assert response.status_code == 201
    
def test_put_invalid_data_format(client):
    assemblies = client.get('http://localhost:5000/products')
    assembly = json.loads(assemblies.json)
    assembly_id = assembly[0]["_id"]["$oid"]
    json_data = json.loads(sample_data.invalid_post)
    response = client.put('http://localhost:5000/product/'+ assembly_id, json=json_data)
    assert response.json == {"error":"Invalid data format"}
    
def test_put_invalid_id(client):
    response = client.put('http://localhost:5000/product/invalid_id')
    assert response.status_code == 404




