# function returning multiple values 
# problem : create a function that returns both the area and 
# circumference of a circle given its radius.

def circle_properties(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

print(circle_properties(5))