file = open("11_file_handling/package/01_simplefile.txt", "r")

file.seek(6)

print(file.read())

file.close()