import requests
import json

BASE = "http://localhost:5000"

response = requests.get(BASE + "/products")
products = json.loads(response.json())
product_id= products[1]["_id"]["$oid"]

response = requests.put(BASE + "/product/" + product_id,json={"stock_level":2,"name":"capacitorrrrrrr", "sub_components":[{"name":"bolt"}]})

response = requests.get(BASE + "/product/" + product_id)
print(response.json())