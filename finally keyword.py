
try:
    num = int(input("Enter the number: "))
    list = [1,2,3,4]
    print(list[num])
except:
    print("some error.")
 # finally:   # the finally portion always executed beshak wo try block mai ho ya execpt mai
print("I am always here to print.")
#      but we can also write the simple print statement without the finally keyword so what is the difference
# the difference is when you wrap the code in the function.

def printing(i):
    try:
        i = int(input("Enter the index: "))
        list1  = [1,2,3,4,5]
        print(list1[i])
        return 1
    except:
        print("There is a error.")
        return 0
    finally:
        print("i a module i am finally keyword i will be always used.")
