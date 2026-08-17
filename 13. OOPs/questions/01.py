class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(
            f"Name    : {self.name}\nRoll No : {self.roll_no}\nMarks   : {self.marks}")

    def update_marks(self, new_marks):
        self.marks = new_marks


student1 = Student("Ansh", 101, 95)

student1.display_details()

student1.update_marks(98)

print("\nAfter Updating Marks:\n")

student1.display_details()