# create parent class

class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)

x = Human("salman", "acting")
x.dowork()

# create child class
class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
  pass # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("ranveer", "acting")
x.dowork()

# add __init__ function to child class
class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
    def __init__(self, name, work):
        Human.__init__(self, name, work)
a = Student("avi", "python developer")
a.dowork()

"""
super() function
Python also has a super() function
that will make the child class inherit
all the methods and properties from its parent:
"""
class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
    def __init__(self, name, work):
        super().__init__(name, work)
a = Student("avi", "python developer")
a.dowork()

# add properties
class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
    def __init__(self, name, work):
        super().__init__(name, work)
        self.dob = (1995)
a = Student("avi", "python developer")
a.dowork()
print(a.dob)

class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
    def __init__(self, name, work):
        super().__init__(name, work)
        self.dob = year
a = Student("avi", "python developer", 1995)
a.dowork()
print(a.dob)

# add method
class Human:
  def __init__(self, name, work):
    self.name = name
    self.work = work

  def dowork(self):
    print(self.name, self.work)
class Student(Human):
    def __init__(self, name, work):
        super().__init__(name, work)
        self.dob = year
    def speak(self):
        print("hello guys my details are", self.name, self.work, self.dob)
a = Student("avi", "python developer", 1995)
a.speak()

