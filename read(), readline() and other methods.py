# f = open("writing.txt",'r')
#
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# This will print the lines

# f = open("Writing.txt",'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     name = line.split(" ")[0]
#     math = line.split(" ")[1]
#     physics = line.split(" ")[2]
#     chemistry = line.split(" ")[3]
#     print(f"Name of student {i} is: {name}")
#     print(f"Math marks of student {i} is: {math}")
#     print(f"Physics marks of student {i} is: {physics}")
#     print(f"chemistry marks of student {i} is: {chemistry}")
#     print(line)
#

# Writing the lines in the file

file = open("myfile.txt",'w')

lines = ["This is line1\n","This is line2\n","This is line1"]

file.writelines(lines)
file.close()

file2 = open("myfile")