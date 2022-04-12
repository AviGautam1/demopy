"""
int is a whole numbers of any range and negative
nad positive number also.
"""
x = 8
y = 35656222554887711
z = -2541

print(type(x))
print(type(y))
print(type(z))

"""
Float, or "floating point number" is a number, 
positive or negative.
"""
x = 2.5
y = 2.00
z = -12.2562
a = 5e2
print(type(x))
print(type(y))
print(type(z))
print(type(a))

"""
Complex numbers are written with a "j" 
as the imaginary part
"""

x = 1+5j
y = 20j
z = -8j

print(type(x))
print(type(y))
print(type(z))

# type coversion

x = 5
y = 2.5
z = 2j

a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)

# it display random value between 2 to 20
import random
print(random.randrange(2, 20))

