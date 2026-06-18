import re

text = "aaa"

print(bool(re.search("a+", text)))

# | Symbol | Meaning   |
# | ------ | --------- |
# | *      | 0 or More |
# | +      | 1 or More |
# | ?      | 0 or 1    |
# | {n}    | Exact n   |
# | {n,m}  | Range     |
