from collections import namedtuple

a = namedtuple('courses', 'name, technology')
s = a('data science', 'python')
print(s)


t = a._make(['artificial intelligence', 'python'])
print(t)

