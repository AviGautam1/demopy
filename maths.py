"""
Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:
"""
x = min(5, 1, 25)
y = max(5, 10, 55)
print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
x = -7.554
print(abs(x))

# The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(5, 8)
print(x)

# python built in module math
import math
x = math.sqrt(25)
print(x)

import math
#Round a number upward to its nearest integer
x = math.ceil(1.4)
#Round a number downward to its nearest integer
y = math.floor(1.4)
print(x)
print(y)

import math
x = math.pi
print(x)