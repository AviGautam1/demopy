# arithmetic operator
x = 10
y = 8
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

# assignment operators
x = 6
x += 8
print(x)

x = 5
x -= 3
print(x)

x = 3
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 10
x%=3
print(x)

x = 12
x//=3
print(x)

# comparison operator
x = 12
y = 11
print(x == y)

x = 5
y = 3
print(x != y)

x = 12
y = 11
print(x > y)

x = 5
y = 3
print(x < y)

x = 12
y = 11
print(x >= y)

x = 5
y = 3
print(x <= y)

# logical operator
x = 8
print(x > 3 and x < 10)

x = 8
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

# identity operator
x = ["avi", "deepak"]
y = ["avi", "deepak"]
z = x
print(z is x)
print(x is z)
print(x is y)
print(x == y)
print(x is not z)
print(x is not y)
print(x != y)

# membership operator
x = ["avi", "deepak"]
print("avi" in x)
print("ankur" not in x)