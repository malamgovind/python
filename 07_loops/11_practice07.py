# validate input
# problem : keep asking the user for input until they enter a number beetween 1 and 10.

while True:
    number = int(input("enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print("thank you for entering a valid number")
        break
    else:
        print("invalid number, please try again.")