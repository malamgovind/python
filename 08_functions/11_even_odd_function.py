def check(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
    
check((int(input("enter a number: "))))