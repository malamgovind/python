class School:

    def info(self):
        print("goverment school")

class Student(School):

    def info(self):
        print("this is student info")

class Teacher(School):

    def info(self):
        print("this is teacher info")

class Principal(School):

    def info(self):
        print("this is principal info")

school = [School(), Student(), Teacher(), Principal()]

for position in school:
    position.info()