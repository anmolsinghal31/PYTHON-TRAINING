#Q1
class Vehicle:
    def start(self):
        print("The vehicle is starting...")

my_vehicle = Vehicle()
my_vehicle.start()


#Q2
class Vehicle:
    def start(self):
        print("The vehicle is starting...")

class Car(Vehicle):
    def drive(self):
        print("The car is driving.")


my_car = Car()
my_car.start()
my_car.drive()

#Q3
class Vehicle:
    count = 0  # This is the class variable

    def __init__(self):
        Vehicle.count += 1



#Q4
class Vehicle:
    def start(self):
        print("Vehicle engine started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Execution
print("--- Single Inheritance ---")
c = Car()
c.start()  # From Parent
c.drive()  # From Child