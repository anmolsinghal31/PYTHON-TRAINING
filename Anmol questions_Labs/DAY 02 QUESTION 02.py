class PositiveSalary:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        instance.__dict__[self.name] = value

class Engineer:
    salary = PositiveSalary('salary')

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

try:
    eng1 = Engineer("Aryan", 70000)
    print(f"Engineer: {eng1.name}, Salary: {eng1.salary}")

    eng2 = Engineer("Sanya", 85000)
    print(f"Engineer: {eng2.name}, Salary: {eng2.salary}")

    eng1.salary = -5000

except ValueError as e:
    print(e)