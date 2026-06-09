with open("11_file_handling/package/01_simplefile.txt", "r") as source:
    content = source.read()
    print(content)

with open("11_file_handling/package/05_copy.txt", "w") as target:
    target.write(content)

print("Copied!")