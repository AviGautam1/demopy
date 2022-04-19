# local scope
def myfunc():
    x = 10
    print(x)
myfunc()

# function inside function
def myfunc():
    x = 20
    def inneerfunc():
        print(x)
    inneerfunc()
myfunc()

# global scope
x = 300
def myfunc():
  print(x)
myfunc()

# naming variable
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

# global keyword
def myfunc():
  global x
  x = 300
myfunc()
print(x)

x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)