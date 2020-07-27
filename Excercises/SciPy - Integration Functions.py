#Integration deals with adding slices to determine the whole
import scipy
from scipy import integrate, special

help(integrate.quad)
print("------------------------")

#quad takes a function as its input
i = scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)
print("------------------------")


#finding double integrals (dblquad)
e = lambda x,y: x*y**2
f = lambda x: 1
g = lambda x: -1
h = integrate.dblquad(e,0,2,f,g)
print(h)
print("------------------------")

