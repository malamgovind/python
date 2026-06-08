# count positive number 
# problem : given a list of number, count how mamy are positive.
# -- number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
number_positive_count = 0

for num in number:
    if num > 0:
        number_positive_count += 1
        print(number_positive_count)
print(number_positive_count)

