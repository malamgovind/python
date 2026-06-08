# find the first non-repeating character
# problem: given a string, find the first non-repeating character.

input_string = input("enter a string: ")

for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print("the first non-repeating character is: ", char)
        break
else: 
    print("there is no non-repeating character in the string.")