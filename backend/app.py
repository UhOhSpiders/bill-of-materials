from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId
from data_validation import product_validator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
client = MongoClient('mongodb://localhost:27017/') 
db = client['bill-of-materials-db'] 
collection = db['data'] 

class Product(Resource):
    def get(self, product_id=None):
        if product_id and ObjectId.is_valid(product_id):
            product_id = ObjectId(product_id)
            result = collection.find({"_id":product_id},{"_id":0, "stock_level": 1, "name": 1, "subassemblies": 1 })
            return dumps(result), 200
        if product_id and not ObjectId.is_valid(product_id):
            return {"error":"Invalid ID"}, 404
        else:
            result = collection.find({},{"_id":1, "stock_level": 1, "name": 1, "subassemblies": 1 })
            return dumps(result), 200
    
    def post(self, product_id=None):
        validated_product = product_validator(request.json)
        if request.json is not validated_product:
            return {"error":"Invalid data format"}, 400
        else:
            collection.insert_one(request.json)
            return "data added", 201
    
    def put(self, product_id):
        if product_id and ObjectId.is_valid(product_id):
            validated_product = product_validator(request.json)
            if request.json is not validated_product:
                return {"error":"Invalid data format"}, 400
            else:
                product_id = ObjectId(product_id)
                collection.update_one({"_id":product_id},{"$set":request.json})
                return "product updated", 201
        else:
            return {"error":"Invalid ID"}, 404
    
api.add_resource(Product, "/product/<string:product_id>","/products")

if __name__ == "__main__":
    app.run(debug=True)