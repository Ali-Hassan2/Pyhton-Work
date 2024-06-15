print("********** CALCULATOR ************************")
print("\n")

print("1. For Addition.")
print("2. For Subtraction.")
print("3. Multiplication.")
print("4. Division.")
print("====================")
x = int(input("Enter the choice: "))

match x:
    case 1:
        y = int(input("Enter the number 1: "))
        z = int(input("Enter the number 2: "))
        print("The Addition is: ",y+z)
    case 2:
        y = int(input("Enter the number 1: "))
        z = int(input("Enter the number 2: "))
        print("The Addition is: ", y - z)
    case 3:
        y = int(input("Enter the number 1: "))
        z = int(input("Enter the number 2: "))
        print("The Addition is: ", y * z)
    case 4:
        y = int(input("Enter the number 1: "))
        z = int(input("Enter the number 2: "))

        if(z <= 0 or z == 0):
            print("cannot perform division on zero.")
        else:
            print("The diviosn is: ",y/z)
    case _:
        print("Enter the correct choice.")

