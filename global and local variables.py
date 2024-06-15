# Local and global variables in Python

x = 4

print("The gloval value of x is: ",x)

def hello():
    # global keyword and this is used to change the value of the global varibale in the function
    global x
    x = 5
    print(f"The locakl variable x value is {x}")
    # This local variable is bounded in the function
#     If i make the local valriable bounded in the function and i call it outside the function then it will not executed
    y = 8
    # as y is in the function and the local variable and cannot be called outdide the function


hello()
print("The x value is: ",x)

x = 6
print(f"Global valriable value of x changes {x}")