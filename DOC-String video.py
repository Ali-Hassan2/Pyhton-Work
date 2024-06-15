# DOC STRINGS IN PYTHON
# THESE ARE NOT THE COMMENTS AND NOT IGNORED
# BY PYTHON
# systax '''content'''
def sum(a,b):
    '''This is a doc string:
    There is a sum which
    will return the sum of
    the two numbers.'''
    print("The sum of two numbers is: ",a+b)
    print("\n")

#     Executing the function()
sum(1,2)
# Printing the docstring in the function
print(sum.__doc__)
# By using this u can trigger the doc string in
# python and it is not used as the comment
# The docstrigs are used to dcument the module
# or the function or the class
# Doc string is the simple concept and most often
# asked in the exams point of view.

