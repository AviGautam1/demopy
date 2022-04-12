# strings are array

x = "hey! there am using python"
print(x[5:9])
print(len(x))

# looping through string
for x in "mercedez":
    print(x)

# check string
x = "work hard to do something"
# print("work" in x)
if "work" in x:
    print("yes")
else:
    print("no")

x = "you are amazing"
print("you" not in x)

# slicing of string
x = "we support huminity"
print(x[3:6])
print(x[:9]) # slicing for the start
print(x[5:]) # slicing from the end
print(x[-12:-8]) # negative index strat from end

x = "hello folk"
print(x.upper()) # return value in upper case

x = "HELLO FOLK"
print(x.lower()) # return value in lower case

x = "  hello folk  "
print(x.strip()) # remove whitespace

x = "jello folk"
print(x.replace("j", "h")) # replace string to another string

x = "hello folk"
print(x.split(",")) # split string into substring and return a list

# concatenation of string
x = "hello"
y = "folk"
z = x + y
print(z)

"""
if you want to space between string use " " 
for it.
"""
x = "hello"
y = "folk"
z = x +  " " + y
print(z)

# format string
x = 2428
y = "my car number is {}"
print(y.format(x))

# we can pass unlimited argument on format
x = 100
y = 75
z = 25
result = "if i have {} rupees and i spent {} rupees so i save {} rupees"
print(result.format(x, y, z))

# using index number
x = 25
y = 100
z = 75
result = "if i have {1} rupees and i spent {2} rupees so i save {0} rupees"
print(result.format(x, y, z))

# escape character
#x = "my name is "avinesh" kumar"
x = "my name is \"avinesh\" kumar"
print(x)

# string methods
x = "my services"
print(x.capitalize()) # convert first letter in capital

x = "MY NAME IS KHAN"
print(x.casefold()) # convert each character in lower case

x = "python"
print(x.center(50, "0")) # will center align string

x = "i love, my country i love it"
print(x.count("love")) # it will return repeating words



