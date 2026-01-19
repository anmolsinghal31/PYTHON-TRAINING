# 1. Base Class: Calculator
class Calculator:
    def calculate(self, a, b):
        print("Base Calculator")
        return a + b

# 2. Subclass: AdvancedCalculator
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("Advanced Calculator")
        return a * b

# 3. Custom Class: Number (Operator Overloading demonstrate karne ke liye)
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

# 4. Polymorphism: Same method name, different behaviors
def show_polymorphism(calc_obj, x, y):
    result = calc_obj.calculate(x, y)
    print(f"Result: {result}")

obj1 = Calculator()
obj2 = AdvancedCalculator()

print("Method Overriding & Polymorphism")
show_polymorphism(obj1, 10, 5) # Base class behavior
show_polymorphism(obj2, 10, 5) # Subclass behavior

print("\nOperator Overloading")
num1 = Number(20)
num2 = Number(30)

total = num1 + num2
print(f"Custom Objects ka sum: {total}")