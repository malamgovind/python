from collections import ChainMap

d1 = {"a":1}
d2 = {"b":2}

result = ChainMap(
    d1,
    d2
)

print(result["a"])
print(result["b"])