"""
==============================
ATTRIBUTES & METHODS
==============================

Attribute
    Variables inside a class.

Method
    Functions inside a class.
"""

class Student:

    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} | {self.grade} | {self.percentage}%")

student = Student("Madhav",11,96)

# View Attributes
print(student.__dict__)

# Modify Attribute
student.percentage = 100

print(student.percentage)

# Delete Attribute
del student.percentage

print(student.__dict__)