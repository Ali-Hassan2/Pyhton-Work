# RECURSION IN PYTHON.

# RECURSION IS A METHOD IN WHICH THE FUNCTION CALL ITSELF.
# THERE IS A BASE CODITION TO STOP THE EXECUTION OF THE PROGRAM AND
# THE PROGRESSIVE APPROACH.

# Program to find the factorial using the recursion.

def factorials(n):

    if(n == 0 or n == 1):
        return 1
    return n * factorials(n-1)

print("The factorial of 5 is: ",factorials(5))

def fib(n):

    if(n == 0):
        return 0
    elif(n == 1 or n==2):
        return 1

    return fib(n-1) + fib(n-2)

print("THE FIB OF 5 is: ",fib(5))