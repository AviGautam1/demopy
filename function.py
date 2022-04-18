# calling a function
def myfunc():
    print("hello")
myfunc()

# function argument
def myfunc(sname):
    print(sname + "correct")
myfunc("avinesh")
myfunc("1200210010")
myfunc("computer science")

# number of arguments is equal to when you called a function
def myfunc(fname, lname, stream):
    print(fname + " " + lname + " " + stream)
myfunc("avi", "gautam", "compter science")

""" use of *args:
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
"""
def myfunc(*info):
    print("the student details" + info[1])
myfunc("avi", "gautam", "cs")

# send argument with key = value syntax
def myfunc(student1, student2, student3):
    print("the student details are" + student2)
myfunc(student1="avi", student2="deepak", student3="ankur")

# arbitary keyword argument **kwargs
def myfunc(**sinfo):
    print("the student details are" + sinfo["lname"])
myfunc(fname = "avinesh", lname = "gautam")

# default parameter value
def myfunc(branch = "cs"):
    print("i am studyng in" + branch )
myfunc("civil")
myfunc("ee")
myfunc()

# passing a list as an argument
def myfunc(student):
    for x in student:
        print(x)
student = ["avi", "deepak", "ankur"]
myfunc(student)

# return value
def myfunc(x):
    return 7 * x
print(myfunc(5))
print(myfunc(8))

# pass statment avoid getting error when function is empty
def myfunc():
    pass

# recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

