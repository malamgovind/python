import csv

with open("11_file_handling/package/03_demo.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["govind", "20"])

with open("11_file_handling/package/03_demo.csv", "r") as file:
   print(file)
   print(file.readlines())