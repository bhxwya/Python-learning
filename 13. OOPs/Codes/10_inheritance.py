"""
==============================
INHERITANCE
==============================

Parent Class
    Existing class.

Child Class
    Reuses Parent class properties and methods.

super()
    Calls the Parent class constructor.
"""

class Student:

    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} | {self.grade} | {self.percentage}%")

class GraduateStudent(Student):

    def __init__(self,name,grade,percentage,stream):
        super().__init__(name,grade,percentage)
        self.stream = stream

    def show_stream(self):
        print("Stream :",self.stream)

student = GraduateStudent("Keshav",12,96,"PCM")

student.student_details()
student.show_stream()