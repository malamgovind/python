import re

text = "123"

print(bool(re.search(r"\d", text)))

# | Sequence | Meaning   |
# | -------- | --------- |
# | \d       | Digit     |
# | \D       | Not Digit |
# | \w       | Word      |
# | \W       | Not Word  |
# | \s       | Space     |
# | \S       | Not Space |
