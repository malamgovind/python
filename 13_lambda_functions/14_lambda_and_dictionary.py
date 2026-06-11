students = {
    "Hari": 80,
    "Govind": 95,
    "Parth": 70
}

result = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(result)