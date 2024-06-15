# FUNCTIONS IN PYTHON
# THE DEF KEYWORD IS USED

def sum(a , b):
    print("The sum of numbers is: ",a+b)

sum(5,7)

def average(*numbers): # this is for tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The average of numbers is: ",(sum)/len(numbers))

average(1,2,3,4,5,6,7)
