# DefaultDict is a dictionary subclass which calls a factory function to supply missing values

from collections import  defaultdict

d = defaultdict(int)

d[1] = 'python'
d[2] = 'edureka'

print(d[3])   # defaultdict will not return an error even if the value is missiong
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
a = {1: 'Python', 2: 'edureka'}
print(a[3])    # dictionary will return an eror