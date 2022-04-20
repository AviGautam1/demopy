"""
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
Python has a built-in package called json, which can be used to work with JSON data.
"""
# If you have a JSON string, you can parse it by using the json.loads() method.
import json
# some JSON:
x = '{ "name":"avi", "age":26, "city":"agra"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON by json.dumps() method.
import json

# a Python object (dict):
x = {
  "name": "avi",
  "age": 26,
  "city": "agra"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

"""
You can convert Python objects of the following types, into JSON strings:
dict
list
tuple
string
int
float
True
False
None
"""

import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))