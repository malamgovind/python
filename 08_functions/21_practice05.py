# defualt parameter value
# problem : write a function that greets a user.
# if no name is provided, it should greet with a default name.

def greet(name):
    if name is None:
        name = "Guest"
    return (f"hello, {name}")

print(greet("Govind"))
print(greet(None))

# second way to do this is by using default value

def greet(name="user"):
    return (f"hello, {name}")

print(greet("Govind"))
print(greet())