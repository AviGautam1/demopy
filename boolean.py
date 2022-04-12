# boolean represent True or False
x = 10
y = 8
if x > y:
    print("yes")
else:
    print("no")

# bool() method evalute any vale and return in True or False
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# except this
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# function can return boolean
def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")