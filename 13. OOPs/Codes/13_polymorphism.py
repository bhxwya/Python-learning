"""
==============================
POLYMORPHISM
==============================

Same method name.

Different behaviour.
"""

class Student:

    def student_details(self):
        print("Student Details")

class GraduateStudent(Student):

    def student_details(self):
        print("Graduate Student Details")

student = Student()
graduate = GraduateStudent()

student.student_details()

graduate.student_details()