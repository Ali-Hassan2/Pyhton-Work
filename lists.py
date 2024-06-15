list1 = [1,2,3,4]
# print(list1)
# print(type(list1))
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

l = [1,2,3,"Ali",False,8.7,23333333323]
print(l)

for i in l:
    print(i)

#     Negative Indexing
li = [1,2,3,4,5]
print("The length is: ",len(li))

print(li[-3])

print(li[len(li)-3])







# Finding anything in the list
marks = [1,2,3,4,5,6,7]

if 7 in marks:
    print("Yes 7 is present.")
else:
    print("No 7 is not present.")

lists = [1,2,3,4,5]
num_to_find = int(input("Enter the number you want to find in the list: "))
if num_to_find in lists:
    print("Yes ",num_to_find," present in the list.")
else:
    print("No ",num_to_find," is not present.")

names = ["Ali","Hassan","shoaib"]

if "Ali" in names:
    print("Yes presnet.")
else:
    print("No not present.")

str = input("Enter the name: ")

if "CODE" in str:
    print("Yes present.")
else:
    print("No")

marks = [1,2,3,4,5,6]
print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:4])
print(marks[1:-1])
print(marks[1:len(marks)-1])

marks2 = [1,2,3,4,5,6,7,8,9]
print(marks2)
print(len(marks2))
for i in marks2:
    print(i)

print(marks2[1:7:2])






