"""
==============================
ABSTRACTION
==============================

Definition:
Hide internal implementation and show only
the necessary functionality.

Example:
User only calls student_details().
How the percentage is calculated is hidden.
"""

class Student:

    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        final_percentage = self.percentage + 2
        print(f"{self.name} scored {final_percentage}%")

student = Student("Madhav",11,96)

student.student_details()