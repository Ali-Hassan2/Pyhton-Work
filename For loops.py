# FOR LOOPS

name = "EACODE"

for i in name:
    print(i)
name2 = "ALI HASSAN"
for i in name2:
    print(i, end = ", ")

# Iterating in the list
list1 = ["APPLE","MANGO", "PINEAPPLE", "GREEN"]
for list in list1:
    print(list)
    for i in list:
        print(i)

# If and for loop
x = "EACODE"
for i in x:
    print(i)
    if(i == "A"):
        print("There is something special.")

# Range function in the for loop

for i in range(5):
    print(i)

for i in range(5):
    print(i+1)   # 1 2 3 4 5

# if i want that my program runs form 1 to 2000 then i will write as for i in range(1,2000)

# for the increment i will use this as (1,2000,3) as of my choice
for i in range(1,100):
    print(i)
# only even numbers
for i in range(0,100,2):
    print(i, end = ", ")


# FACTORIAL BY FOR LOOP IN PYTHON

fact = 1;
num = int(input("Enter the number: "))

for i in range(1,num+1,1):
    fact = fact * i
print("The factorial of the number is: ",fact)

