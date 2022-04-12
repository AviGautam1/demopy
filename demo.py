x = 5
y = "fruit"
print(x)
print(y)
print(type(x))
print(type(y))

# Assigning multiple values
x, y, z = "honda", "jupiter", "suzuki"
print(x)
print(y)
print(z)

x = "honda", "jupiter", "suzuki"
print(x)

# unpacking values
list = ["lion", "dog", "cat"]
x, y, z = list
print(x)
print(y)
print(z)

# output variables

x = 10
y = "sanjeev"
print(x,y)

# global variables

x = "deepak"
def myfunc():
    x = "ankur"
    print(x)
myfunc()
print(x)

def myfunc():
    global x
    x = "udit"
myfunc()
print(x)

