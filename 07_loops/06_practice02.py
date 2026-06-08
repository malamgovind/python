# sum of the even numbers
# problem : calculate the sum of the even number up to a given number n.

n = int(input("enter your number: "))
sum_even = 0

for x in range(1, n+1):
    if x%2 == 0:
        sum_even += 1

print("the sum of the even number up to a number n is: ", sum_even)