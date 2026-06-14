class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

person = Person("Govind")

print(person.name)

# person.name
#     │
#     ▼
# @property detect
#     │
#     ▼
# name(self) call
#     │
#     ▼
# return self._name
#     │
#     ▼
# "Govind"
#     │
#     ▼
# print()