# len(students)
# ↓
# students.__len__()
# ↓
# 100

class Student:
    
    def __len__(self):
        return 100

student = Student()
print(len(student))