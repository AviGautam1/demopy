# tuple alloe any data type
tuple = ("apple", 5, "mango", True)
print(tuple)

# tuple constructor
tuple = (("apple", 5, "mango", True))
print(tuple)
print(len(tuple))
print(type(tuple))

# tuple with one value dont forget to put comma
tuple = ("apple",)
print(type(tuple))

# access tuple items
tuple = ("apple", "mango", "kiwi", "banana")
print(tuple[1])
print(tuple[1:3])
print(tuple[1:])
print(tuple[:1])
print(tuple[-3:-2])

# check item present or not
tuple = ("apple", "mango", "kiwi", "banana")
if "papaya" in tuple:
    print("yes")
else:
    print("no")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# unpack tuple
car = ("tata", "honda", "tesla")
(x , y , z) = car
print(x)
print(y)
print(z)

car = ("tata", "honda", "tesla", "maruti", "suzuki")
(x , y , *z) = car
print(x)
print(y)
print(z)

car = ("tata", "honda", "tesla", "maruti", "suzuki")
(x , *y , z) = car
print(x)
print(y)
print(z)

# loop through for loop
car = ("tata", "honda", "tesla", "maruti", "suzuki")
for x in car:
    print(x)

# loop through index number
car = ("tata", "honda", "tesla", "maruti", "suzuki")
for x in range(len(car)):
    print(car[x])

# loop through while loop
car = ("tata", "honda", "tesla", "maruti")
x = 0
while x < len(car):
    print(car[x])
    x = x + 1

# join tuple
car1 = ("tata", "honda", "tesla", "maruti", "suzuki")
car2 = ("jupiter", "range rover")
car = car1 + car2
print(car)

# multiply tuple
car = ("tata", "honda", "tesla", "maruti", "suzuki")
x = car * 2
print(x)





