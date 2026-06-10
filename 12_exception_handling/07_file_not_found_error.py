try:
    file = open("11_file_handling/package/01_simplefile.txt")
    print(file.read())
    file2 = open("11_file_handling/package/01_simplefile01.txt")

except FileNotFoundError:
    print("file not found")