"""
====================================================
17. MAGIC (DUNDER) METHODS
====================================================

Official Name:
Special Methods

Also Known As:
• Magic Methods
• Dunder Methods

Dunder = Double Under(score)

Examples

__init__()
__str__()
__repr__()
__len__()
__eq__()
__add__()

====================================================
Why do we need Magic Methods?
====================================================

Magic methods tell Python how custom
objects should behave when built-in
operations are used.

Python automatically calls these methods.

We usually DO NOT call them directly.

====================================================
Example 1 : __init__()
====================================================
"""

class Student:

    def __init__(self, name):
        self.name = name


student = Student("Ansh")

print(student.name)

"""
Output

Ansh

__init__()

↓

Automatically called when an object
is created.

Student("Ansh")

↓

Student.__init__("Ansh")
"""


"""
====================================================
Example 2 : __str__()
====================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Ansh")

print(student)

"""
Output

Ansh

Without __str__()

↓

<__main__.Student object at 0x...>

With __str__()

↓

Ansh

Python secretly does

print(student)

↓

student.__str__()
"""


"""
====================================================
Example 3 : __repr__()
====================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name='{self.name}')"


student = Student("Ansh")

print(student)

"""
Output

Student(name='Ansh')

__repr__()

returns a detailed representation
of the object.

Mostly useful for debugging.
"""


"""
====================================================
Example 4 : __len__()
====================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


student = Student("Ansh")

print(len(student))

"""
Output

4

Python secretly does

len(student)

↓

student.__len__()
"""


"""
====================================================
Example 5 : __eq__()
====================================================
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


student1 = Student("Ansh")
student2 = Student("Ansh")
student3 = Student("Rahul")

print(student1 == student2)
print(student1 == student3)

"""
Output

True
False

Python secretly does

student1 == student2

↓

student1.__eq__(student2)
"""


"""
====================================================
Example 6 : __add__()
====================================================
"""

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


student1 = Student(90)
student2 = Student(95)

print(student1 + student2)

"""
Output

185

Python secretly does

student1 + student2

↓

student1.__add__(student2)
"""


"""
====================================================
Normal Method vs Magic Method
====================================================

Normal Method

student.display()

↓

Called by Programmer


Magic Method

print(student)

↓

Called Automatically by Python
"""


"""
====================================================
Quick Revision
====================================================

Student()

↓

__init__()


-----------------------

print(student)

↓

__str__()


-----------------------

len(student)

↓

__len__()


-----------------------

student1 == student2

↓

__eq__()


-----------------------

student1 + student2

↓

__add__()
"""


"""
====================================================
Interview Notes
====================================================

Q. What are Magic Methods?

Magic methods are special methods that
allow Python to automatically perform
built-in operations on custom objects.

Q. Who calls Magic Methods?

Python automatically calls them.

Q. Why are they called Dunder Methods?

Because their names start and end
with double underscores (__).

Example

__init__()
__str__()
"""


"""
====================================================
One Line to Remember
====================================================

Magic Methods are instructions that tell
Python how custom objects should behave
when built-in operations are used.
"""