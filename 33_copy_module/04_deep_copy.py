import copy 

a = [1, 2, 3]

b = copy.deepcopy(a)

b.append(4)

print(a)
print(b)