class animal:
    def sound(self):
        print("I am animal")

class dog(animal):
    def sound(self):
        print("I am dog")

class cat(animal):
    def sound(self):
        print("I am cat")
obj=[dog(),cat()]

for a in obj:
    a.sound()