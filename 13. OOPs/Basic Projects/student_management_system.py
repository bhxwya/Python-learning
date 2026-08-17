class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(
            f"Name     : {self.name}\nRoll no. : {self.roll_no}\nMarks    : {self.marks}")

    def update_marks(self, updated_marks):
        self.marks = updated_marks

    def __str__(self):
        return (
            f"{self.name}(Roll no. : {self.roll_no})")


class StudentManagementSystem:
    def __init__(self,):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(student)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display_details()
                return
        print("Student not found")

    def update_student_marks(self, roll_no, new_marks):
        for student in self.students:
            if student.roll_no == roll_no:
                student.update_marks(new_marks)
                print("Marks updated successfully.")
                return
        print("Student not found")

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found")


sms = StudentManagementSystem()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))

        student = Student(name, roll_no, marks)
        sms.add_student(student)

        print("Student added successfully.")

    elif choice == "2":
        sms.display_students()

    elif choice == "3":
        roll_no = int(input("Enter the student roll number: "))
        sms.search_student(roll_no)

    elif choice == "4":
        roll_no = int(input("Enter the student roll number: "))
        new_marks = int(input("Enter the updated marks: "))
        sms.update_student_marks(roll_no, new_marks)

    elif choice == "5":
        roll_no = int(input("Enter the student roll number: "))
        sms.delete_student(roll_no)

    elif choice == "6":
        print("Thank you for using Student Management System.")
        break
    
    else:
        print("Invalid Choice. Please try again.")
