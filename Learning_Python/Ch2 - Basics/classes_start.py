#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

from msilib.schema import Class
#from typing_extensions import Self


class Vehicle():
    def __init__(self, bodysytle):
        self.bodystyle = bodysytle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class moto(Vehicle):
    def __init__(self, enginetype, sidecar):
        super().__init__("Motorcycle")
        if (sidecar):
                self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "moto at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = moto("gas", True)

print(mc1.wheels)
#3
print(car1.enginetype)
#gas
print(car2.doors)
#4

car1.drive(30)
car2.drive(40)
mc1.drive(50)