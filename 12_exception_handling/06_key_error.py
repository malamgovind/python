student = {
    "name" : "Govind",
    "age"  : 20
}

try:
    print(student["name"])
    print(student["age"])
    print(student["city"])

except:
    print("key not found")