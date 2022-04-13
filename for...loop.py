car = ["maruti", "tesla", "ford"]
for x in car:
    print(x)

# looping through string
for x in "mercedez":
    print(x)

# break statement
car = ["maruti", "tesla", "ford"]
for x in car:
    print(x)
    if x == "tesla":
        break

# continue statement
car = ["maruti", "tesla", "ford"]
for x in car:
    if x == "tesla":
        continue
    print(x)

# range() function
for x in range(10):
  print(x)

for x in range(2, 10):
  print(x)

for x in range(6 , 50 , 2):
  print(x)

# else in for loop
for x in range(8):
    print(x)
else:
    print("finished")

for x in range(8):
    if x == 5: break
    print(x)
else:
    print("finished")

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x)
    print(y)

# pass statement
for x in [0, 1, 2]:
  pass
