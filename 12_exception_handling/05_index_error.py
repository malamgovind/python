num = [10, 20, 30]

try:
    print(num[3])

except IndexError:
    print("index out of range")