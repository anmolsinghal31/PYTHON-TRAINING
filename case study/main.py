import csv
import json


# --- 1. DESCRIPTOR (Data Validation) ---
class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance._salary

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        instance._salary = value


# --- 2. BASE CLASS (Inheritance) ---
class Person:
    def __init__(self, name, department):
        self.name = name
        self.department = department


# --- 3. STUDENT CLASS (Operator Overloading & Destructors) ---
class Student(Person):
    def __init__(self, sid, name, dept, semester, marks):
        super().__init__(name, dept)
        self.sid = sid
        self.semester = semester
        self.marks = marks

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = 'A' if avg >= 80 else 'B' if avg >= 60 else 'C'
        return avg, grade

    def get_details(self):
        avg, grade = self.calculate_performance()
        return f"[Student] ID: {self.sid} | Name: {self.name} | Avg: {avg} | Grade: {grade}"

    def __del__(self):
        print(f"[Cleanup] Student record {self.sid} removed from memory.")


# --- 4. FACULTY CLASS (Descriptor & Polymorphism) ---
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, dept, salary):
        super().__init__(name, dept)
        self.fid = fid
        self.salary = salary

    def get_details(self):
        return f"[Faculty] ID: {self.fid} | Name: {self.name} | Dept: {self.department} | Salary: {self.salary}"

    def __del__(self):
        print(f"[Cleanup] Faculty record {self.fid} removed from memory.")


# --- 5. COURSE CLASS ---
class Course:
    def __init__(self, code, name, credits, faculty_name):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty_name = faculty_name


# --- 6. MANAGEMENT SYSTEM ---
class UniversitySystem:
    def __init__(self):
        self.students = {}
        self.faculties = {}
        self.courses = {}

    def add_student(self):
        sid = input("Student ID: ")
        name = input("Student Name: ")
        dept = input("Department: ")
        sem = input("Semester: ")
        marks = list(map(int, input("Marks (5 subjects space separated): ").split()))
        self.students[sid] = Student(sid, name, dept, sem, marks)
        print(f"Student {name} Added Successfully!")

    def add_faculty(self):
        fid = input("Faculty ID: ")
        name = input("Faculty Name: ")
        dept = input("Department: ")
        try:
            sal = float(input("Monthly Salary: "))
            self.faculties[fid] = Faculty(fid, name, dept, sal)
            print(f"Faculty {name} Added Successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def add_course(self):
        code = input("Course Code: ")
        name = input("Course Name: ")
        creds = int(input("Credits: "))
        fid = input("Faculty ID for this course: ")
        if fid in self.faculties:
            self.courses[code] = Course(code, name, creds, self.faculties[fid].name)
            print(f"Course '{name}' Added Successfully!")
        else:
            print("Error: Faculty ID not found! Create Faculty first.")

    def enroll_student(self):
        sid = input("Enter Student ID: ")
        ccode = input("Enter Course Code: ")
        if sid in self.students and ccode in self.courses:
            print(f"Enrollment Successful: {self.students[sid].name} enrolled in {self.courses[ccode].name}")
        else:
            print("Error: Invalid Student ID or Course Code!")

    def search_record(self):
        search_id = input("Enter Student or Faculty ID to search: ")
        if search_id in self.students:
            print(f"Match Found: {self.students[search_id].get_details()}")
        elif search_id in self.faculties:
            print(f"Match Found: {self.faculties[search_id].get_details()}")
        else:
            print("Record not found.")

    def compare_two_students(self):
        id1 = input("First Student ID: ")
        id2 = input("Second Student ID: ")
        if id1 in self.students and id2 in self.students:
            s1, s2 = self.students[id1], self.students[id2]
            avg1, _ = s1.calculate_performance()
            avg2, _ = s2.calculate_performance()
            print(f"\n--- Comparison ---")
            if avg1 > avg2:
                print(f"RESULT: {s1.name} ({avg1}) is HIGHER than {s2.name} ({avg2})")
            elif avg1 < avg2:
                print(f"RESULT: {s1.name} ({avg1}) is LOWER than {s2.name} ({avg2})")
            else:
                print(f"RESULT: Both have EQUAL marks ({avg1})")
        else:
            print("Error: Student IDs not found!")

    def delete_record(self):
        did = input("Enter ID to delete: ")
        if did in self.students:
            del self.students[did]
            print("Student record deleted.")
        elif did in self.faculties:
            del self.faculties[did]
            print("Faculty record deleted.")
        else:
            print("ID not found.")

    def generate_reports(self):
        with open('students_report.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Dept", "Avg", "Grade"])
            for s in self.students.values():
                avg, grade = s.calculate_performance()
                writer.writerow([s.sid, s.name, s.department, avg, grade])
        print("Reports generated in students_report.csv")


# --- 7. MAIN MENU ---
if __name__ == "__main__":
    system = UniversitySystem()
    while True:
        print("\n" + "=" * 40)
        print(" UNIVERSITY MANAGEMENT SYSTEM MENU ")
        print("=" * 40)
        print("1. Add Student         2. Add Faculty")
        print("3. Add Course          4. Enroll Student")
        print("5. Search Record       6. Compare Students")
        print("7. Delete Record       8. Generate Reports")
        print("9. Exit")

        choice = input("\nSelect Option (1-9): ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.add_faculty()
        elif choice == '3':
            system.add_course()
        elif choice == '4':
            system.enroll_student()
        elif choice == '5':
            system.search_record()
        elif choice == '6':
            system.compare_two_students()
        elif choice == '7':
            system.delete_record()
        elif choice == '8':
            system.generate_reports()
        elif choice == '9':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid Choice!")