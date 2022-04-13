a = 20
b = 15
if a > b:
    print("yes")
else:
    print("no")

"""use of elif shows if previous 
condition not true try next condition"""
a = 50
b = 50
if a > b:
    print("yes")
elif a == b:
    print("no")

# short hAND IF
a = 10
b = 5
if a > b: print("yes")

# short hand if else
a = 50
b = 49
print("greater") if a > b else print("lower")

# AND and OR uses
a = 15
b = 12
c = 10
if a > b and b > c:
    print("both conditions are true")

a = 15
b = 12
c = 10
if a > b or b < c:
    print("one comdition is true")

a = 15
b = 12
c = 10
if a > b and b < c:
    print("both conditions are true")

# nested if
a = 50
if a > 40:
    print("yes")
    if a < 100:
        print("yes")
    else:
        print("no")

# pass statement
a = 33
b = 200

if b > a:
  pass