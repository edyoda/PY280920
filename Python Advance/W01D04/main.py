# import mod1
# from mod1 import *

# //* means import everything from that module.

# output = spacex("land us on mars")

# print(output)

# output2 = google("make an amazing search engine")

# print(output2)

# print(pipi)


# Question/Activity: make a module mod2.py, write functions microsoft,netflix , import mod2
# functions and use
# them in main.py file.

# 7 Minutes
# 8:10PM


# import mod2
# result = mod2.microsoft("use servers inside marines in deep sea")

# movie = mod2.netflix("HeraPheri")

# print(result)
# print(movie)

# we can import the modules if they are present in:
# 1) Same directory
# 2) Python Sys path


# import sys

# print("We can import modules from these paths =>")

# for i in sys.path:
# 	print(i)


# import math
# import mod2

# print(math.pi)

# print(dir(math))

# print(dir(mod2))

# print(mod2.__file__)

# import math as mathematics  #alias

# print(math.pi)

# print(mathematics.pi)


# globals() and locals()

# import math

# print(help(math))


#without initialisation file(__init__ file)
# import package # it does not work

# print(package.mod3.ibm("make a quantum computer"))

# from package import mod3

# print(mod3.ibm("make a quantum computer"))

# print("before import",dir())
# import package.mod3
# print("after import",dir())


# print(mod3.ibm("make a quantum computer"))

# from package import mod3 as module_we_want

## Package Initialisation.
# Once done, we get follwoing benefits:
# 1) Now if you import package, you can import all the modules 
# which are present inside that package.
# 2) It can initialise some pre requisites.


## from package import * + __all__ list in init file in package.
# import package
from package import *
print(mod3.ibm("make us an Quantum Computer"))

