class Employee:

    def work(self):
        print("employee working")

class Manager(Employee):
    
    def manage(self):
        print("manage team")

manager = Manager()
manager.work()