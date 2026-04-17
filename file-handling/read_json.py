import json

with open("data/sample.json", "r") as f:
    data = json.load(f)

print(data)
