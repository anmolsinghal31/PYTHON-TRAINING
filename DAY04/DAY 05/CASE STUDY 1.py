import json

# 1. Base Class (Inheritance)
class Person:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}"

# 2. Student Class (Method Overriding & Operator Overloading)
class Student(Person):
    def __init__(self, id, name, dept, marks):
        super().__init__(id, name, dept)
        self.marks = marks # List of marks

    # Method Overriding (Polymorphism)
    def get_details(self):
        return f"Student: {self.name} | Dept: {self.dept}"

    # Operator Overloading (Comparison)
    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# 3. Faculty Class
class Faculty(Person):
    def __init__(self, id, name, dept, salary):
        super().__init__(id, name, dept)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name} | Dept: {self.dept}"

# 4. Generator (Iterators)
def get_student_names(students):
    for s in students:
        yield s.name

# --- Testing the System ---

# Objects create karna
s1 = Student("S101", "Ananya", "CS", [80, 90, 85])
s2 = Student("S102", "Rohan", "CS", [70, 75, 80])
f1 = Faculty("F201", "Dr. Rajesh", "CS", 85000)

# Polymorphism check
print(s1.get_details())
print(f1.get_details())

# Operator Overloading check
print(f"Is Ananya better than Rohan? {s1 > s2}")

# Generator check
names_gen = get_student_names([s1, s2])
print("Student List:", list(names_gen))

# Exception Handling & File Saving
try:
    with open("data.json", "w") as f:
        json.dump({"student": s1.name, "dept": s1.dept}, f)
    print("File saved successfully!")
except Exception as e:
    print(f"Error occurred: {e}")