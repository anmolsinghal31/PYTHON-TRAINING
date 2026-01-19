class Parent:
    def parent1(self):
        print("Parent 1")

class Child(Parent):
    def child1(self):
        print("Child1")

class Child2(Parent):
    def child2(self):
        print("Child2")

c1 = Child()
c1.child1()
c1.parent1()

c2 = Child2()
c2.parent1()
c2.child2()
