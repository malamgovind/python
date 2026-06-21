from collections import Counter

data = ["a", "b", "a", "c", "a"]

result = Counter(data)

print(result)

# a b a c a
# ↓
# Counter()
# ↓
# a = 3
# b = 1
# c = 1