from functools import reduce

result = reduce(lambda a, b: a + b, [1, 2, 3, 4])

print(result)

## --- memory flow 

# 1 + 2 = 3

# 3 + 3 = 6

# 6 + 4 = 10