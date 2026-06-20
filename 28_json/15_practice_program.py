import json

data = {
    "country":"India",
    "state":"Gujarat"
}

json_data = json.dumps(data)

print(json_data)