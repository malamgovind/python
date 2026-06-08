# recursive function 
# problem : create a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))