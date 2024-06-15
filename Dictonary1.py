# DICTONARY IN PYTHON

dict1 = {"Ali":"Male", "she": "woman"}
print(dict1)
print(dict1["Ali"])
# I can perform the mapping of any object.
# 2nd way is
print(dict1.get("Ali"))

dict2 = {"marks1":15, "marks2": 20, "marks3": 25}
# if i want to take all the keys i can use this
print(dict2.keys())

#  By the iteration from the loop
# Keys are marks1, marks2, marks3

for i in dict2.keys():
    print(i)
    print(dict2[i])
# By the f-string i can print this like that
    print(f"The value of the corresponding {i} is {dict2[i]}")