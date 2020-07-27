import datetime

#Create some date element
print(datetime.datetime(2020,7,24,4,12,2,100))
print("-------------------------------")

#Display today's date
print(datetime.datetime.today())
print("-------------------------------")

#Display today's date
print(datetime.datetime.now())
print("-------------------------------")

#Access some particualar value of date
v = datetime.datetime.now()
print(v.year)
print(v.day)
print(v.hour)
print("-------------------------------")

#set only date without time
x = datetime.date(2020,7,24)
print(x)
print("-------------------------------")

#set only time without date
x = datetime.time(3,7,24)
print(x)
print("-------------------------------")