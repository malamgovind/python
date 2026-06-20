import json

student = {
    "name":"Govind",
    "marks":90
}

json_data = json.dumps(student)

print(json_data)