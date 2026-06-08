# function with *args
# problem : write a function that takes variable number of 
# arguments and returns their sum.'

def sum_all(*args):
    print(*args)
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3,4,5))