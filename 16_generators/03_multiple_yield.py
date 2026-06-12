def fruit():
    yield "apple"
    yield "banana"

for f in fruit():
    print(f)