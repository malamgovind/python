with open("11_file_handling/package/01_simplefile.txt", "wb") as file:
    file.write(b"python")


with open("11_file_handling/package/01_simplefile.txt", "rb") as file:
    data = file.read()
    print(data.decode())