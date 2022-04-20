import modules
modules.greeting("Jonathan")

import modules

a = modules.person1["age"]
print(a)

# re naming modules by using alias as keyword
import modules as info

a = info.person1["age"]
print(a)

# built in modules
import platform

x = platform.system()
print(x)

# using dir() function
import platform

x = dir(platform)
print(x)

"""
You can choose to import only parts from a module, by using the from keyword
"""
from modules import person1

print (person1["age"])