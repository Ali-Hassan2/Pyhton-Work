# F-Strings in Python
info = "My name is {1} and I am from {0}."
place = "World"
# Formating by the old manner
print(info.format("EACODE", place))
# Formatting problem
print(info.format(place, "EACODE"))
#                        0     1
print(info.format(place, "EACODE"))
# Syntx for creating the f-string in python
print(f"My name is EACODE and i am from{place}.")
# operations performing in the f-string
print(f"The sum of 2 and 3 is {2+3}")
print(f"The sub of 2 and 3 is: {2-3}")
print(f"The Mul of 2 and 3 is: {2*3}")
