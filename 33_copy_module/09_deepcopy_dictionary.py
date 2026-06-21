import copy

a = {
    "student": {
        "name": "Govind"
    }
}

b = copy.deepcopy(a)

b["student"]["name"] = "Hari"

print(a)
print(b)