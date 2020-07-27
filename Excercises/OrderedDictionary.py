# Order dictionalry is a dictionary subclass which remembers the orders in which the orders were done

from collections import  OrderedDict

d = OrderedDict()

d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'

print(d)
print(d.keys())
print(d.items())
print(d.__len__())
print(d.__str__())

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(d)
d[1] = 'p'
print(d)
