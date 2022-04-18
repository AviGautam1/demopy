# create a class by using class keyword
class myinfo:
    x = "avi"
a = myinfo()
print(a.x)

class myinfo:
    x = "avi"
myinfo()
print(myinfo().x)

# create objects
class myinfo:
    x = "avi"
a = myinfo() # object with name a
print(a.x)

# the __init__ function
"""class Human:
    def __int__(self, n, o):
        self.name = n
        self.occupation = o
    def work(self):
        if self.occupation == "sport":
            print(self.name, "cricket")
        elif self.occupation == "actor":
            print(self.name, "acting")
    def speaks(self):
        print(self.name, "says how are you ?")
tom = Human("salman khan", "sport")
tom.work()
tom.speaks()"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# modify objects properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

# delete object properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)

# delete object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)

