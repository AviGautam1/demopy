a = 0
while a < 10:
    print(a)
    a+=1

# break statement
a = 10
while a < 20:
    print(a)
    if a == 15:
        break
    a+=1

# continue statement
a = 0
while a < 10:
    a+=1
    if a == 8:
        continue
    print(a)

# else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
