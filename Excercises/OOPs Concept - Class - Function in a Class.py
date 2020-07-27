class Car():
    def __init__(self, modelname, year_manf, price):    # a constructor
        self.modelname = modelname
        self.year_manf = year_manf
        self.price = price
    def price_inc(self):
        self.price= int(self.price*1.15)

#Create Objects that belongs to the class
honda = Car('City', 2017, 100000)
tata = Car('Bolt', 2016, 60000)

honda.cc = 15000

print(honda.price)
honda.price_inc()
print(honda.price)

