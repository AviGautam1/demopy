# python lambda

x = lambda a : a + 55
print(x(5))


# Lambda functions can take any number of arguments:
x = lambda a, b : a + b
print(x(5, 10))

x = lambda a, b, c : a * b * c
print(x(5, 10, 15))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
