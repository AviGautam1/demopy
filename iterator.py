# tuple, list, dict etc. are iterable objects
list = ["mango", "orange", "banana"]
a = iter(list)
print(next(a))
print(next(a))
print(next(a))

# even string is iterable object
mystr = "avinesh"
a = iter(mystr)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# looping through iterator
list = ["mango", "orange", "banana"]
for x in list:
    print(x)

# create an iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# stopiteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)