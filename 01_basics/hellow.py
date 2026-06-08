from operator import index

from hellow_word import gd

gd("hwllo Govind")

name_type = {
    'malam': 'govind',
    'baraiya': 'parth',
    'mokariya': 'ajay'
}

for name in name_type:
    print(name)

    
    
    name01 = ["govind", "parth", "ajay"]

    for name00 in name01:
        print(name00)

new_name = dict.fromkeys(name01)

for name in name01:
    new_name[name]= name.upper()
print(new_name)


a = 10
print(type(a))
print(a)

a = "Govind"
print(a)
print(type(a))