import json

data = {
    "name":"Govind",
    "age":22
}

json_data = json.dumps(data)

print(json_data)
print(type(json_data))

# Dictionary
# ↓
# dumps()
# ↓
# JSON String