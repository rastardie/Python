# Number Stream

a = range(100)
b = (x for x in a)
print(b)
for y in b:
    print(y)

print("------------------------")

# Even Numbers
a = range(2,100,2)
b = (x for x in a)
print(b)
for y in b:
    print(y)

print("------------------------")

# Odd Numbers
a = range(1,100,2)
b = (x for x in a)
print(b)
for y in b:
    print(y)

print("------------------------")