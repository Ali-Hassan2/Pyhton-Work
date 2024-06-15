import math

result = math.sqrt(9)

print("The square root of 9 is: ",result)

# From keyword:
# we can also import the certain options using the
# from keyword for example if you want to use only
    # sqrt function form the math us can use it as:

from math import pi

radius  = 6

area = pi * radius * radius

print("The aresa is: ",area)

# To import eveythin in the library we can use *
# from math import *

# as keyword:

# this is used to make the small function trigging nam

from math import sqrt as s
result = s(9)
print(result)

#  Dir function:
import math

print(dir(math))

print(math.sqrt, type(math.sqrt))

# from Functions_in_python import greater
from ali import hello, name

hello()

print(name)
