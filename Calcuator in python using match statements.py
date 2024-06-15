
print("********************* CALCULATOR ************************")
print("\n")

print("1. For Addition.")
print("2. For Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("====================")
x = int(input("Enter the choice: "))

match x:
    case 1:
        y = int(input("Enter the first number: "))
        z = int(input("Enter the second number: "))
        print("The Addition of the Two numbers is: ",y+z)
    case 2:
        y = int(input("Enter the first number: "))
        z = int(input("Enter the second number: "))
        print("The Addition of the Two numbers is: ", y - z)
    case 3:
        y = int(input("Enter the first number: "))
        z = int(input("Enter the second number: "))
        print("The Addition of the Two numbers is: ", y * z)
    case 4:
        y = int(input("Enter the first number: "))
        z = int(input("Enter the second number: "))
        if(z <= 0 or z == 0):
            print("Cannot perform the division operation.")
        else:
            print("The Division of Two numbers is: ",y/z)
    case _:
        print("Enter the correct option.")



