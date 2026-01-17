class Student:
    # 1. Defining attributes name and roll_no using a constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # 2. Method to print student information
    def display_details(self):
        print(f"Student Name: {self.name} | Roll Number: {self.roll_no}")

# 3. Creating at least two objects of the class
student1 = Student("Alice Smith", 101)
student2 = Student("Bob Johnson", 102)

# Displaying their details
student1.display_details()
student2.display_details()