from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name", "age"]
)

s1 = Student(
    "Govind",
    22
)

print(s1.name)

# Tuple

# ↓

# namedtuple

# ↓

# Attribute Access