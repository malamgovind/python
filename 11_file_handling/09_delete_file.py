import os 

if os.path.exists("11_file_handling/package/_simplefile.txt"):
    os.remove("11_file_handling/package/01_simplefile.txt")
    print("delete")

else:
    print("file not found ")