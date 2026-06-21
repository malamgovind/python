import copy

numbers = [10, 20]

new_numbers = copy.copy(
    numbers
)

new_numbers.append(30)

print(numbers)
print(new_numbers)