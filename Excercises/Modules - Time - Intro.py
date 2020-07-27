import time

t = time.time()  #returns the number of seconds since the epoch (1970)
print(t)
print("--------------------------")

#convet t to current date time.
t2 = time.ctime(t)
print(t2)

print("--------------------------")

#Find helpful info about a time function.
h = help(time.time)
print(h)
print("--------------------------")

#Return local time
lt = time.localtime()  #displays time in struc_time format
print(lt)
print("--------------------------")

#Return seconds from epoch to date
lt = time.localtime()
mt = time.mktime(lt)
print(mt)
print("--------------------------")

#Return time in local time from struct_time
lt = time.localtime()
c = time.asctime(lt)
print(c)
print("--------------------------")

#Return format quotes for returning datetime strings
st = help(time.strftime)
print(st)
print("--------------------------")

#Return customizsed date format
x = time.strftime("%m/%d/%Y")
print(x)
print("--------------------------")

#Return a normal date in s struc_time format
y = "08 August 2020"
s = time.strftime(y, "%d %B %Y")
print(s)
