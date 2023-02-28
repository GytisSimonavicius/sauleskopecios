class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{self.first_name} {self.last_name}"
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

employee = Employee("Elton", "John")
print(employee.fullname)
print(employee.email) 