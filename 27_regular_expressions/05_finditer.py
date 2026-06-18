import re

text = "cat bat rat"

matches = re.finditer("at", text)

for match in matches:
    print(match.start())