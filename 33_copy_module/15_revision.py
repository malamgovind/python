import copy

a = [[1, 2]]

b = copy.deepcopy(a)

b[0].append(5)

print(a)
print(b)