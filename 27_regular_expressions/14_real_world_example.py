import re

text = "Order 123 Cost 500"

numbers = re.findall(r"\d+", text)

print(numbers)