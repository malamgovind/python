# sub()

# ↓

# Search + Replace

import re

text = "I like Java"

result = re.sub(
    "Java",
    "Python",
    text
)

print(result)