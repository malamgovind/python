def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):
        yield a,b

        a, b = b, a + b
        # (a, b) = (b, a + b)

for num in fibonacci(8):
    print(num)
    
# a=0 b=1
#  ↓
# a=1 b=1
#  ↓
# a=1 b=2
#  ↓
# a=2 b=3
#  ↓
# a=3 b=5
#  ↓
# a=5 b=8