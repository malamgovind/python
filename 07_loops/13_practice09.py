# list uniqueness checker
# problem : -- check if elements in a list are unique. 
#           -- if a duplicate is found, exit the loop and print duplicate.
#           -- items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]
unique_items = set()

for item in items:
    if item in unique_items:
        print(f"duplicate found: {item}")
        break
    else:
        unique_items.add(item)