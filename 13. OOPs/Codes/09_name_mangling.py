"""
Name Mangling
"""

class Student:

    def __init__(self):
        self.__marks = 90


student = Student()

print(student.__dict__)


"""
Python changes

__marks

↓

_Student__marks

This is called Name Mangling.

It prevents accidental access and
avoids conflicts during inheritance.

It is NOT true security.
"""