import json

response = '''
{
    "status":"success",
    "message":"Data Found"
}
'''

data = json.loads(response)
print(data)
print(data["status"])