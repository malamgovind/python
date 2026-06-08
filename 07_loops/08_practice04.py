# reverse a string 
# problem: reverse a string using a loop.

input_string = input("enter a string: ")
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("the reversed string is: ", reversed_string)