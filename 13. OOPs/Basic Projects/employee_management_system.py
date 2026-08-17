class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(
            f"Employee Id  : {self.employee_id}\nName         : {self.name}\nDepartment   : {self.department}\nSalary       : {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary

    def __str__(self):
        return(f"{self.name} (ID: {self.employee_id})")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print("No Employees")
            return
        for employee in self.employees:
            print(employee)

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.display_details()
                return
        print("Employee not found.")

    def update_employee_salary(self, employee_id, new_salary):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.update_salary(new_salary)
                print("Salary Updated successfully")
                return
        print("Employee not found.")

    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")


ems = EmployeeManagementSystem()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        employee_id = int(input("Enter the Employee Id: "))
        name = input("Enter the Employee Name: ")
        employee_department = input("Enter the Employee department: ")
        salary = int(input("Enter the Employee Salary: "))

        employee = Employee(employee_id, name, employee_department, salary)
        ems.add_employee(employee)

        print("Employee added successfully")

    elif choice == "2":
        ems.display_employees()

    elif choice == "3":
        employee_id = int(input("Enter the Employee Id:"))
        ems.search_employee(employee_id)

    elif choice == "4":
        employee_id = int(input("Enter the Employee Id: "))
        salary = int(input("Update Employee Salary: "))
        ems.update_employee_salary(employee_id, salary)

    elif choice == "5":
        employee_id = int(input("Enter the Employee Id: "))
        ems.delete_employee(employee_id)

    elif choice == "6":
        print("Thank you for using Employee Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")
