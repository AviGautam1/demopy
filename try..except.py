#The try block will generate an error, because x is not defined:

try:
  print(x)
except:
  print("no error occured")

# you can define many exceptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

"""
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")