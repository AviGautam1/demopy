"""
python does not have any built in method
 for array but we use list instead.
"""
student = ["avi", "deepak", "ankur"]
print(student)

# access the element of an array
student = ["avi", "deepak", "ankur"]
print(student[1])

# modify the array value
student = ["avi", "deepak", "ankur"]
student[1] = "atul"
print(student)

# length of an array
student = ["avi", "deepak", "ankur"]
print(len(student)) # Note: The length of an array is always one more than the highest array index.

# looping through an array
student = ["avi", "deepak", "ankur"]
for x in student:
    print(x)

# adding array elements
student = ["avi", "deepak", "ankur"]
student.append("atul")
print(student)

# removing array elements
student = ["avi", "deepak", "ankur", "atul"]
student.pop(1)
print(student)

student = ["avi", "deepak", "ankur"]
student.remove("deepak")
print(student)