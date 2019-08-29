x = 1   #int
y = 2.8   #float
z = 1j   #comlex
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 45245147555522
z = -5484132554
print(type(x))
print(type(y))
print(type(z))

x = 2.66
y = 52.36
z = 5.256
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 5j
y = +5j
z = -7j
print(type(x))
print(type(y))
print(type(z))

x = 5
y = 2.3
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,10))