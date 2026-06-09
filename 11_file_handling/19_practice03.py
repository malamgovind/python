with open("11_file_handling/package/01_simplefile.txt", "r") as file:
    lines = file.readlines()

print("Lines:", len(lines))