"""
Class Attributes

A class attribute belongs to the class
and is shared by all objects.
"""

class Student:

    school = "ABC Public School"

    def __init__(self, name):
        self.name = name


student1 = Student("Madhav")
student2 = Student("Vishakha")

print(student1.school)
print(student2.school)

student1.school = "XYZ School"

print(student1.school)
print(student2.school)
print(Student.school)