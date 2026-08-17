"""
Methods

A method is a function defined inside a class.
"""

class Student:

    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} scored {self.percentage}%")

    def increase_marks(self):
        self.percentage += 5


student = Student("Ansh", 90)

student.student_details()

student.increase_marks()

student.student_details()