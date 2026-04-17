import json

data = '{"name": "John", "age": 25}'
parsed = json.loads(data)

print(parsed["name"])


me='''
{
    "me":[
    {
    "name":"Mika",
    "job":"struggling"
    }]
}
'''

data=json.loads(me)#string->object
print(type(data))
print(data['me'])
print(data['me'][0]['name'])
print(data)
