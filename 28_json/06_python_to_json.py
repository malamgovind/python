import json

student = {
    "name":"Hari",
    "city":"Jamnagar"
}

json_data = json.dumps(student)

print(json_data)