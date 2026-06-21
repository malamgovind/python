import copy 

student = ["malam", "govind"]


backup = copy.deepcopy(student)

backup.append("devshibhai")

print(student)
print(backup)