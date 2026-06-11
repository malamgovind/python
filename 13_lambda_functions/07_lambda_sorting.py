students = [
    ("govind", 20),
    ("parth", 21)
]

students.sort(key = lambda x: x[1])
print(students)
print(type(students))