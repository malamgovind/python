try:
    num = int(input("enter a number: "))
    print(num)

except ValueError:
    print("only number allowed")