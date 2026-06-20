import json

data = {
    "language":"Python"
}

with open("28_json/000_language.json","w") as file:
    json.dump(data,file)