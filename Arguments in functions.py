def average(a = 5, b = 7):
    print("The average of two numbers is: ", (a+b)/2)

average(1,5)
average(b=3)
average(a = 1)

# THE EXAMPLE
def name(fname, midname = "Hassan", lname = "waris"):
    print("The name is: "+fname+ " "+midname+" "+lname)

fname = "Ali"
mid_name = "Hassan"
lname = "Waris"
name(fname,mid_name,lname)
name("Shoaib", "Hassan")


set1 = {1,2,3,4,5,6}
set2 = {7,8,9}

# IF I WANT TO FIND THE AVERAGE OF A LARGE NUMBERS THEN I WILL PASS THE TUPLE AS

def average2(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The averge of the numbers is: ", (sum)/len(numbers))

average2(5,4,5,54,3,1)


def name(*names):
    for i in names:
        print(names)
        for j in i:
            print(j)

name("ALI","Hassan")


def sum(*numbers): # The numbers are passesd as the touple
    sum = 0
    for i in numbers:
        sum+=i

    return sum


c = sum(5,3,2,4,6,2)
print("The sum is: ",c)






