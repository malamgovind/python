import re

text = "Govind learns Python"

if re.search("Python", text):
    print("Found")
else:
    print("Not Found")