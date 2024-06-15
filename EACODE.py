# FUNCTION TO PRINT THE SUM
def sum_of_number(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

numbers = []

while True:
    inp = input("Enter the numbers as according to EMAN 0 to finish: ")
    num = int(inp)

    if(num == 0):
        break
    #     it will add the entered numbers to the list of numbers
    numbers.append(num)

if numbers:
    res = sum_of_number(*numbers)
    print("The sum is: ",res)
else:
    print("No input.")