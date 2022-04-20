"""
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
"""
import re
txt = "my name is avinesh gautam"
x = re.search("^my.*gautam$", txt)
if x:
    print("match")
else:
    print("no match")

# findall() function
import re
txt = "my name is avinesh gautam"
x = re.findall("a", txt)
print(x)

# If no matches are found, an empty list is returned:
import re
txt = "my name is avinesh gautam"
x = re.findall("z", txt)
print(x)

# search() function
import re
txt = "my name is avinesh gautam"
x = re.search("\s", txt)
print("the first white space on", x.start())

import re
txt = "my name is avinesh gautam"
x = re.search("z", txt)
print(x)

# The split() function returns a list where the string has been split at each match:
import re
txt = "my name is avinesh gautam"
x = re.split("\s", txt)
print(x)

# split on second occurence
import re
txt = "my name is avinesh gautam"
x = re.split("\s", txt, 2)
print(x)

# The sub() function replaces the matches with the text of your choice:
import re
txt = "my name is avinesh gautam"
x = re.sub("\s", "2", txt)
print(x)

# Replace the first 2 occurrences:
import re
txt = "my name is avinesh gautam"
x = re.sub("\s", "2", txt, 2)
print(x)