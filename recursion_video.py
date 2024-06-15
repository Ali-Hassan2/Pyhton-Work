# RECURSION IN PYTHON.
# RECURSION IS A PROCESS IN WHICH A FUNCTION
# CALL if ITSELF.
# IT CONTAIN THE BASE CONDITION AND THE PROGRESSIVE
# APPROACH.

# PERFORMING THE FACTORIAL EXAMPLE BY RECURSION

def factorial(n):

    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

# FIBBONACI SERIES EXAMPLE

def fib(n):
    if(n == 0):
        return 0
    if n == 1 or n == 2:
        return 1

    return fib(n-1) + fib(n-2)


print("The factorial of 5 is: ",factorial(5))

