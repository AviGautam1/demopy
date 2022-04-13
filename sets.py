# python set
set = {"tata", 5, True, "ford", "range rover"}
print(set)
print(len(set))
print(type(set))

# set constructor
set = (("tata", 5, True, "ford", "range rover"))
print(set)

# access items
set = {"tata", "ford", "tesla", "suzuki"}
for x in set:
    print(x)

set = {"tata", "ford", "tesla", "suzuki"}
if "tesla" in set:
    print("yes")

# add otems
set = {"tata", "ford", "tesla", "suzuki"}
set.add("range rover")
print(set)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter"}
set1.update(set2)
print(set1)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = ["land rover", "jupiter"]
set1.update(set2)
print(set1)

# remove set items
set = {"tata", "ford", "tesla", "suzuki"}
set.remove("tesla")
print(set)

set = {"tata", "ford", "tesla", "suzuki"}
set.discard("range rover")
print(set)

set = {"tata", "ford", "tesla", "suzuki"}
set.pop()
print(set)

set = {"tata", "ford", "tesla", "suzuki"}
del set
print(set)

set = {"tata", "ford", "tesla", "suzuki"}
set.clear()
print(set)

# join sets
set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter"}
set = set1.union(set2)
print(set)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter", "ford"}
set1.update(set2)
print(set1)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter", "ford"}
set1.intersection_update(set2)
print(set1)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter", "ford"}
set = set1.intersection(set2)
print(set)

set1 = {"tata", "ford", "tesla", "suzuki"}
set2 = {"land rover", "jupiter", "ford"}
set1.symmetric_difference_update(set2)
print(set1)



