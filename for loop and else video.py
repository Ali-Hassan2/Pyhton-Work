# Finally keyword in Python
#  this is used as in some cases witht the exception so the finally block is always executed in all cases
def even():
    try:
        num = int(input("Enter the number: "))

        if num % 2 == 0:
            return 1
        else:
            return 0
    except ValueError:
        print("There is a <type> error.")
# Now here i can use the finally keyword and make a block of code which always be executed in all cases
#  i can also do this it also will always executed with try and except but there is a issue when we wrap this
#     code int the module it will not be executed and we have to use the finally keyword there.
    finally:
        print("i will always be executed.")

display = even()
print(display)
#  In this case the finally block not executed so we have to use the finally keyword