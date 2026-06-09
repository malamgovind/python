file = open("11_file_handling/package/01_simplefile.txt", "r")

print(file.tell())

file.read(5)

print(file.tell())

file.close()