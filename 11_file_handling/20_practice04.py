word = "Python"

with open("11_file_handling/package/01_simplefile.txt", "r") as file:
    content = file.read()

if word in content:
    print("Word Found")
else:
    print("Word Not Found")