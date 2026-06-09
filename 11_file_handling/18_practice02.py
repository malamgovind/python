with open("11_file_handling/package/01_simplefile.txt", "r") as file:
    word = file.read().split()

print("Word: ", len(word))