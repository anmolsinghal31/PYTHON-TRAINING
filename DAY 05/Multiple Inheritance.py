class A:
    def showA(self):
        print("Dog")

class B:
    def showB(self):
        print("Cat")

class C(A,B):
    pass

c=C()
c.showA()
c.showB()