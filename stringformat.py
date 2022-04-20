# Add a placeholder where you want to display the price:
x = 26
y = "my age is {}"
print(y.format(x))

# You can add parameters inside the curly brackets to specify how to convert the value:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# And add more placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# use index number
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))