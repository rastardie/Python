# A chainmap is used to create a single view of multiple mappings

from collections import  ChainMap

# create two dictionaris
a = {1: 'edureka', 2: 'python'}
b = {3: 'ML', 4: 'AI'}

# assign a and b to a ChaninMap
a1 = ChainMap(a,b)
print(a1)