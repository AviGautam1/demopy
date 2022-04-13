dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
print(dict)

# refer to key
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
print(dict["age"])

# dict can not allow same key value
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science",
    "branch" : "civil"
}
print(dict)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
print(len(dict))
print(type(dict))

# dict allow any data type
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science",
    "colour" : ["red", "green"]
}
print(dict)

# access item
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.get("branch")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.keys()
print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.keys()
dict["roll number"] = 1234
print(x)

# return only values
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.values()
print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.values()
print(x)
dict["roll number"] = 1234
print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.items()
print(x)

# update items
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
dict.update({"roll number" : 1234})
print(dict)

# remove items
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
dict.pop("age")
print(dict)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
dict.popitem()
print(dict)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
del dict["branch"]
print(dict)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
dict.clear()
print(dict)

# loop dict
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x in dict:
    print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x in dict:
    print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x in dict:
    print(dict[x])

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x in dict.keys():
    print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x in dict.values():
    print(x)

dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
for x , y in dict.items():
    print(x , y)

# copy dict
dict = {
    "name" : "avi",
    "age" : 25,
    "branch" : "computer science"
}
x = dict.copy()
print(x)

# nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}