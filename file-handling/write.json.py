import json

data = {"name": "A", "marks": [80, 90]}

with open("data/sample.json", "w") as f:
    json.dump(data, f)

