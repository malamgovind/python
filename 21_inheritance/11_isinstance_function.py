# isinstance() Python નું built-in function છે.
# તે ચેક કરે છે કે કોઈ object કોઈ ચોક્કસ class નું instance છે કે નહીં, અથવા inheritance દ્વારા તેની parent class નું instance છે કે નહીં.

# isinstance(object, class)
# object = જે object ચેક કરવો છે
# class = જે class સામે ચેક કરવું છે

class Parent:
    pass

class Child(Parent):
    pass

child = Child()
print(isinstance(child, Child))
print(isinstance(child, Parent))