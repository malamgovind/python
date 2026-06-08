# prime number checker
# problem : check if a number is prime or not.

number = int(input("enter a number: "))
this_prime = True

if number > 1:
    for x in range(2, number):
        if number % x == 0:
            this_prime = False
            break
        else:
            this_prime = True
else:
    this_prime = False

if this_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
