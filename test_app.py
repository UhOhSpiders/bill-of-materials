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

# GET Methods:

# Test getting a single product by ID:

# Send a GET request to /product/<valid_product_id>.
# Assert the status code is 200 (OK).
# Assert the response data contains the expected product information (name, stock level, subassemblies).
# Test with an invalid product ID (e.g., non-existent ID) and assert a 404 (Not Found) status code.
# Test getting all products:
def test_post(client):
    json_data = json.loads(sample_data.valid_post)
    response = client.post('http://localhost:5000/products',json=json_data)
    assert response.status_code == 201
# Send a GET request to /products.
# Assert the status code is 200 (OK).
# Assert the response data is a list and contains multiple product entries.
# Optionally, test for specific product names or other details depending on your data.
def test_get_all(client):
    response = client.get('http://localhost:5000/products')
    assert response.status_code == 200
    if response.status_code == 200:
        result = json.loads(response.json)
        assert isinstance(result, list)


# POST Method:

# Test creating a new product with valid data:

# Send a POST request to /products with a valid JSON object representing a product (refer to your validation schema).
# Assert the status code is 201 (Created).
# Optionally, check the response message (if any) for success confirmation.
# Test creating a product with invalid data:

# Send a POST request with invalid data (missing fields, invalid formats, etc.) that should fail validation.
# Assert the status code is 400 (Bad Request).
# Assert the response contains an error message indicating the validation failure.
# PUT Method:

# Test updating a product with valid data:

# Send a PUT request to /product/<valid_product_id> with a valid JSON object representing the updated product details.
# Assert the status code is 201 (Created or Updated). (Note: This API uses 201 for PUT as well)
# Optionally, verify if the product data in the database reflects the changes.
# Test updating a product with invalid data:

# Send a PUT request with invalid data that should fail validation.
# Assert the status code is 400 (Bad Request).
# Assert the response contains an error message indicating the validation failure.
# Test updating a non-existent product:

# Send a PUT request to a non-existent product ID.
# Assert the status code is 404 (Not Found).
# Additional Considerations:

# Use a testing framework like pytest to structure your tests effectively.
# Mock or isolate external dependencies like the database connection for reliable testing.
# Consider testing edge cases and error handling scenarios.
# Remember to replace placeholders like <valid_product_id> with actual values in your tests.
