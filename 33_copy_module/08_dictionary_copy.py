import copy

a = {
    "name": "Govind"
}

b = copy.copy(a)

b["name"] = "Hari"

print(a)
print(b)