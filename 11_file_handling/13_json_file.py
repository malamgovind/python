import json

student = {
    "name": "Govind",
    "age": 20
}

with open("11_file_handling/package/04_demo.json", "w") as file:
    json.dump(student, file, indent=4)


with open("11_file_handling/package/04_demo.json", "r") as file:
    print(json.load(file))