company = {
    "IT": {
        "rahul": {"salary": 55000, "experience": 3},
        "arjun": {"salary": 70000, "experience": 5},
    },
    "HR": {
        "priya": {"salary": 60000, "experience": 4},
        "neha": {"salary": 65000, "experience": 6},
    },
    "Sales": {
        "rohan": {"salary": 50000, "experience": 2},
        "sara": {"salary": 75000, "experience": 5},
    },
}
highest_salary = 0
employer_name = ""
department = ""

for sectors, employees in company.items():
    for employees_name, employees_details in employees.items():
        employees_salary = employees_details["salary"]
        if employees_salary > highest_salary:
            highest_salary = employees_salary
            employer_name = employees_name
            department = sectors

print(
    f"Employee: {employer_name} \nDepartment: {department} \nSalary: {highest_salary}")
