from abc import ABC, abstractmethod

class Shape(ABC):
    def display(self):
        print("Normal shape")
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        print("Area method implemented")


r = Rectangle()
r.area()
r.display()

