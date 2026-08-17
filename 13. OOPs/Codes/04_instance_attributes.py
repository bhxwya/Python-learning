"""
Instance Attributes

An instance attribute belongs to an individual object.

Each object has its own copy of instance attributes.
"""

class Student:

    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage


student1 = Student("Madhav", 11, 96)
student2 = Student("Vishakha", 12, 99)

print(student1.name)
print(student2.name)

student1.name = "Ansh"

print(student1.name)
print(student2.name)