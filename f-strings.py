# F-strings in Python.

info = "My name is {1} and i am from {0}."
name = "Ali Hassan"
place = "Pakistan"

print(info.format(name,place))
#                        0     1
# PROBLEM IN THE FORMETTING.
print(info.format(place,name))
#  To solve this probelm i can number in the {} in the string.
print(info.format(place,name))

# The syntax for creating the f-string is f"My name is {variable_name} and i am from {variable_name}."

print(f"My name is {name} and i am from {place}.")

print(f"The sum of 2 + 3 is: {2+3}")
name2 = "ALI HASSAN"
place_to_study = "CS"
year = 5
info2 = f"I am {name2} and I am studing {place_to_study} and year is {year}"
print(info2)

