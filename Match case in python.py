x = 4

match x:
    case 0:
        print("x is zero.")
    case 4:
        print("x is 4.")
    case _:
        print("Enter the correct value.")


# i can also add the if condition in the cases

x2 = int(input("Enter the number: "))

match x:
    case 1:
        print("Number is 1.")
    case 5:
        print("Number is 5.")
    case _ if x!= 90:
        print("Number is not 90.")
    case _ if x!=80:
        print("Number is not 80.")
    case _:
        print("Enter the correct number.")


