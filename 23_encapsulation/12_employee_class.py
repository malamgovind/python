class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

employee = Employee(50000)

print(employee.get_salary())