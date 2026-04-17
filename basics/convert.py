import json

data = {"city": "Delhi", "temp": 35}
json_str = json.dumps(data)

print(json_str)

my={"name":"Mika",
    "job":"struggling"}
print(json.dumps(my))#object->json string
