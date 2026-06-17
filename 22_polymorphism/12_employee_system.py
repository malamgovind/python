class Employee:

    def work(self):
        print("employee working")

class Manager(Employee):

    def work(self):
        print("management team")

class Developer(Employee):

    def work(self):
        print("developer team")

class Boss(Employee):

   pass

company = [Employee(), Manager(), Developer(), Boss()]

for worker in company:
    worker.work()