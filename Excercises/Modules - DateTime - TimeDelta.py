import datetime

#Datetime manipulations
b1 = datetime.timedelta(days=20)
b2 = datetime.timedelta(days=30)
b3 = b1 - b2
print(b3)
print(type(b3))
print("-------------------------------")