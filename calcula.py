def calculator(a , b):
    print("1. For Addition.")
    print("2. For Subtraction.")
    print("Enter the choice: ")
    ch = int(input())

    match ch:
        case 1:
            print("The addition is: ", a + b)
        case 2:
            print("The result is: ",a-b)
        case _:
            print("You are a gay.")

calculator(1,3)