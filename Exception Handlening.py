#
# #  Exception Handlening
#
# print("Enter the number: ")
# num = int(input())
#
# print(f"The multiplication table of {num} is: ")
#
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")
#
#
# num2 = input("Enter the numbers: ")
# print(f"The table of {num2} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(num2)} X {i} = {int(num2)*i}")
# except Exception as e:
#     print(e)                  # it will tell that which error is occured you can also give some random statements
#     print("Sorry bhai erroe hai koi.")
#
#
# try:
#     num3 = int(input("Enter the numbers: "))
# except ValueError:
#     print("Error input valid <type>")

    #  I can handle multiple of errors
try:
    num3 = int(input("Enter the number: "))
    list = [4,3]
    print(list[num3])
except ValueError:
    print("Enter the integer value.")
except IndexError:
    print("There is the index error.")