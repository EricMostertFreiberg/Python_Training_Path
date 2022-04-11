# car example


class Car:
    def __init__(self, engine, wheels, mpg = 10):
        self.engine = engine
        self.wheels = wheels
        self.mpg = mpg
    
    def engineType(self):
        if self.engine == "auto":
            self._engineFactor = .75
            return self._engineFactor
        elif self.engine == "manual":
            self._engineFactor = 2
            return self._engineFactor
        else:
            self._engineFactor = 1
            return self._engineFactor
    
    def wheelsCondition(self):
        if self.wheels == "good":
            self._wheelsFactor = 2
            return self._wheelsFactor
        elif self.wheels == "bad":
            self._wheelsFactor = .5
            return self._wheelsFactor
        else:
            self._wheelsFactor = 1
            return self._wheelsFactor

    def calcMPG(self):
        self.engineType()
        self.wheelsCondition()
        return self.mpg * self._engineFactor * self._wheelsFactor

c1 = Car("auto","bad") #3.75
c2 = Car("manual","good") #40
c3 = Car("asdf","asdf") #10
c4 = Car("manual","bad") #10
c5 = Car("auto","good", 50) #75
print(c1.calcMPG())
print(c2.calcMPG())
print(c3.calcMPG())
print(c4.calcMPG())
print(c5.calcMPG())