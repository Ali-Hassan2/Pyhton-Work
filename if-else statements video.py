# Implementation of Nested if-else in python

# conditional statements
num = int(input("Enter the number: "))
print("The number is: ",num)

#Nested if-else
if(num>=0):
    if(num>=0 and num<=10):
        print("The number is between 0 to 10.")
    elif(num>=10 and num<=20):
        print("The number is between 10 to 20.")
    else:
        prin("Number is greater then 20.")
elif(num == 0):
    print("Number is zero.")
else:
    print("Number is negative.")
