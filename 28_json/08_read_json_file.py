import json 

with open("28_json/000_data.json", "r") as file:
    data = json.load(file)

print(data)