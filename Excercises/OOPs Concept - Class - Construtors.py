#Create the Class
class Car():
    def __init__(self, modelname, year_manf, price):    # a constructor
        self.modelname = modelname
        self.year_manf = year_manf
        self.price = price
#Create Objects that belongs to the class
honda = Car('City', 2017, 100000)
tata = Car('Bolt', 2016, 60000)

honda.cc = 15000  #creae a cc object for honda outside of -init-

print(honda.__dict__)  #get all the methods of an object
print(tata.__dict__)

print("--------------")

print(honda.price)

