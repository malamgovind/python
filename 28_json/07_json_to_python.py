import json

json_data = '''
{
    "name":"govind",
    "city":"Jamnagar"
}
'''

student = json.loads(json_data)
print(student)
print(student["name"])