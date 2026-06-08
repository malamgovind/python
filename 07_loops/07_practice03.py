# multiplication table printer
# problem : print the multiplication table for a given number up to 10, 
# but skip fifth interation.

number = int(input("enter your multiplication table number: "))

for x in range (1, 11):
    if x == 5:
        continue       # skip kare che interation 5 ne and continue to next iteration 
    print(number, 'x', x, '=', number * x)
