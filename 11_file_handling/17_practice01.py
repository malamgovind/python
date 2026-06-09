with open("11_file_handling/package/01_simplefile.txt", "r") as file:
    content = file.read()

print("Character: ", len(content))