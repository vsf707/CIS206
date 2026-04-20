class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    def set_name(self, name):
        self.name = name

    def set_idNumber(self, idNumber):
        self.idNumber = idNumber

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position

    def get_name(self):
        return self.name

    def get_idNumber(self):
        return self.idNumber

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position

    def display(self):
        return f"{self.name:<15} {self.idNumber:<10} {self.department:<15} {self.position:<15}"

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print(f"{'Name':<15} {'ID':<10} {'Department':<15} {'Position':<15}")
print("-" * 60)

print(emp1.display())
print(emp2.display())
print(emp3.display())