#Encapsulation is the method of binding data and code together
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def price_inc(self):
        pass

#SuperCar new attributes and to inherit attributes of Car
class SuperCar(Car):
    def __init__(self, modelname,year_manf,price,cc):
        super.__init__(modelname,year_manf,price)
        self.cc = cc
    def price_inc(self):
        self.price = int(self.price*2)

honda = SuperCar('City', 2017, 100000)
tata = Car('Bolt', 2016, 60000)

honda.cc = 15000

print("---------------------")

print(help(honda))
