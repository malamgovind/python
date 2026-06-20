import json

json_data = '''
{
    "name":"Govind",
    "age":22
}
'''

data = json.loads(json_data)

print(data)
print(type(data))

# JSON String
# ↓
# loads()
# ↓
# Dictionary