from cerberus import Validator

def product_validator(value):
  schema = {
    "name": {"type": "string", "required": True},
    "stock_level": {"type": "integer", "min": 0},
    "subassemblies": {
      "type": "list",
      "schema": {
          "type": "dict",
          "schema": {
          "name": {"type": "string", "required": True},
          "complete": {"type": "boolean", "required": True},
          "cost": {"type": "integer", "min":0},
          "components":{
            "type":"list",
            "schema":{
              "type":"dict",
              "schema":{
                "name":{"type":"string","required":True},
                "stock_level": {"type": "integer", "required": True, "min":0},
                "cost": {"type": "integer", "required": True, "min":0}
              }
            }
          }
        }
      }
      
      }
  }
  v = Validator(schema)
  if v.validate(value):
    return value
  else:
    return None
    