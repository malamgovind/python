import re

text = "cat"

print(bool(re.search("c.t", text)))


# | Symbol | Meaning       |
# | ------ | ------------- |
# | .      | Any Character |
# | ^      | Start         |
# | $      | End           |
# | *      | 0 or More     |
# | +      | 1 or More     |
# | ?      | Optional      |
# | {}     | Exact Count   |
# | []     | Character Set |
# | |      | OR            |
