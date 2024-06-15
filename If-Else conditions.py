# Conditional statements

a = int(input("Enter the age: "))
print("The age is: ",a)

# Conditional statements

print(a>18)
print(a>=18)
print(a<18)
print(a<=18)

if(a>=18):
    # THe space before the statement is called intentation.
    print("Yes, u can drive.")
    print("YES")
else:
    print("No,you cannot drive.")
    print("NO")
print("This statement is not in the if bock and will be executed everytime")

# Example

appleprice = 300
budget = 290

if(appleprice <= budget):
    print("Ali, cannot add the apples in the cart.")
elif(appleprice - budget < 20):
    print("It's ok you can buy.")
else:
    print("Ali can add the apples to the cart.")

# Example 2

num = int(input("Enter the number: "))

if(num>=0):
    print("Number is positive.")
elif(num == 0):
    print("Number is zero.")
else:
    print("Number is negative.")


# Nested Else if
num = int(input("Enter the number: "))
if(num <= 0):
    print("Number is negative.")
elif(num >=0):
    if(num>=0 and  num<=10):
        print("Number is between 0 and 10.")
    elif(num>=10 and num<=20):
        print("Number is between 10 and 20.")
    else:
        print("Number is greater then 20.")
else:
    print("Number is zero.")
