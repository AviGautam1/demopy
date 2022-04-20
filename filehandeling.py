# open the file which is saved in demo.txt
myfile = open("demo.txt", "r")
print(myfile.read())

# read only one line use readline()
myfile = open("demo.txt", "r")
print(myfile.readline())
print(myfile.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
myfile = open("demo.txt", "r")
for x in myfile:
    print(x)

# close file
myfile = open("demo.txt", "r")
for x in myfile:
    print(x)
myfile.close()

# write to an existing file
myfile = open("demo.txt", "a")
myfile.write("file has more contents")
myfile.close()
myfile = open("demo.txt", "r")
print(myfile.read())

myfile = open("demo.txt", "w")
myfile.write("file has more contents")
myfile.close()
myfile = open("demo.txt", "r")
print(myfile.read())

# delete file
import os
os.remove("demo.txt")

# Check if file exists, then delete it:
import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
else:
  print("The file does not exist")

