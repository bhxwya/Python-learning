"""
==============================
ENCAPSULATION
==============================

Definition:
Protect data by restricting direct access.

Private Variable
    __variable

Getter
    Used to access private data.
"""

class Student:

    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage

    def get_percentage(self):
        return self.__percentage

student = Student("Madhav",11,96)

print(student.get_percentage())

# Not Allowed
# print(student.__percentage)