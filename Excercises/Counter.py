# A counter is used to count hashable objects

from collections import  Counter

a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
c = Counter(a)

print(c)

print('&&&&&&&&&&&&&&&&&&&&&')
print(list(c.elements()))   # returns the counter ordered ASC

print('&&&&&&&&&&&&&&&&&&&&&')
print(c.most_common())      # get assorted list of most common elements

print('&&&&&&&&&&&&&&&&&&&&&')
sub = {2:1, 6:1}
print(c.subtract(sub))
print(c.most_common())  # sub removed from the counter

