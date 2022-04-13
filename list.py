studentList = ["atul", "aashu", "udit", "rahul"]
print(studentList)

# list allow dublicate value
studentList = ["atul", "aashu", "udit", "rahul", "aashu"]
print(studentList)

# list allow any value
studentList = ["atul", "aashu", "udit", "rahul", 5, True]
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul"]
print(len(studentList)) # length of the list

# list constructor
studentList = (("atul", "aashu", "udit", "rahul")) # use double quates
print(type(studentList))

# access list items by using index number
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
print(studentList[2])
print(studentList[2:5])
print(studentList[2:])
print(studentList[:2])
print(studentList[-5:-2])

# check item is present or nit
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
if "udit" in studentList:
    print("yes")
else:
    print("no")

# change list item
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList[1] = "sonu"
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList[1:3] = ["sonu", "amit"]
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList[1:2] = ["sonu", "amit"]
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList[1:3] = ["sonu"]
print(studentList)

# by using insert()

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.insert(3, "amit")
print(studentList)

# add list items
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.append("sonu")
print(studentList)

studentList1 = ["atul", "aashu", "udit", "rahul", "manish"]
studentList2 = ["sonu", "mahesh"]
studentList1.extend(studentList2)
print(studentList1)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove list items
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.remove("manish")
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.pop(1)
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.pop()
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
del studentList[1]
print(studentList)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
del studentList

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
studentList.clear()
print(studentList)

# looping the  for loop
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
for x in studentList:
    print(x)

studentList = ["atul", "aashu", "udit", "rahul", "manish"]
for x in range(len(studentList)):
    print(studentList[x])


# looping through while loop
studentList = ["avi", "deepak", "ankur", "himanshu", "zeeshan"]
x = 0
while x < len(studentList):
    print(studentList[x])
    x = x + 1

studentList = ["avi", "deepak", "ankur", "himanshu", "zeeshan"]
[print(x) for x in studentList]

# without list comrehension
studentList = ["avi", "deepak", "ankur", "himanshu", "zeeshan"]
newlist = []
for x in studentList:
    if "h" in x:
        newlist.append(x)
print(newlist)

# with list comrehension
studentList = ["avi", "deepak", "ankur", "himanshu", "zeeshan"]
newlist = [x for x in studentList if "h" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# sort list
studentList = ["avi", "deepak", "ankur", "himanshu", "zeeshan"]
studentList.sort()
print(studentList)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy the list
studentList = ["atul", "aashu", "udit", "rahul", "manish"]
newlist = studentList.copy()
print(newlist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# join list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)