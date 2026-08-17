"""
==============================
CLASSES & OBJECTS
==============================

Class
    Blueprint for creating objects.

Object
    Instance of a class.

Constructor (__init__)
    Automatically runs whenever an object is created.

self
    Refers to the current object.
"""

class Student:

    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}")
        print(f"Percentage : {self.percentage}%")

student1 = Student("Madhav",11,96)
student2 = Student("Vishakha",12,99)

student1.student_details()
student2.student_details()