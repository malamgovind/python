# Custom module import કરો.

import importlib

custom_module = importlib.import_module("13_custom_module")

print(custom_module.add(10, 5))
print(custom_module.sub(10, 5))