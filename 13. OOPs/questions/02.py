class Employee:
    company = "Google"
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Company : {self.company}\nName    : {self.name}\nSalary  : {self.salary}")


employee1 = Employee("Ansh", 50000)
employee2 = Employee("Rahul", 60000)

employee1.display_details()
print()
employee2.display_details()

Employee.company = "Microsoft"
print("\nAfter changing company:\n")

employee1.display_details()
print()
employee2.display_details()

