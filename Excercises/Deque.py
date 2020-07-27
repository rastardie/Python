# Deque is an optimized list for performing insertions and deletions easily

from collections import deque

a = ['e', 'd', 'u', 'r', 'e', 'a']
d = deque(a)
print(d)

print('&&&&&&&&&&&&&&&&&&&&&')

d.append('python')  # Append a value to deque
print(d)  # the deque has a new value

print('&&&&&&&&&&&&&&&&&&&&&')

a = ['e', 'd', 'u', 'r', 'e', 'a']
d = deque(a)
d.appendleft('python') # append a value to the beginning of the deque
print(d)

print('&&&&&&&&&&&&&&&&&&&&&')

a = ['e', 'd', 'u', 'r', 'e', 'a']
d = deque(a)
d.appendleft('python') # append a value to the beginning of the deque
print(d)
d.pop()    # pop removes the value from the end of the deck
print(d)

print('&&&&&&&&&&&&&&&&&&&&&')

a = ['e', 'd', 'u', 'r', 'e', 'a']
d = deque(a)
d.appendleft('python') # append a value to the beginning of the deque
print(d)
d.popleft()    # popleft removes the leftmost value from the deck
print(d)