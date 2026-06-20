import json

data = {
    "name":"Govind",
    "age":22
}

with open("0_data.json","w") as file:
    json.dump(data,file)

    # data.json file create થશે