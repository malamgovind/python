from collections import Counter

text = "python python java"

words = text.split()

result = Counter(words)

print(result)