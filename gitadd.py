print("Hello")

list = [1,2,3,4,5]

index = 0

for i in list:
    print(i)
    if i == 2:
        print("it is 2.")
    if index == 2:
        print("it is t number2.")
    index= index + 1

num = int(input("Enter the number: "))

fact = 1

for i in range(1,num+1):
    fact = fact * i

print("The factorial of the number is: ",fact)
