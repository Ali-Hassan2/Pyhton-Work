 


# Reading the file
# f = open("writing.txt" , 'r')
# # R mode is for the reading the data from the file
# text = f.read()
# print(text)
# f.close()

# w mode for the writing the file
# a for the append mode and the data will not be overwritten

file = open("writing.txt",'a')
file.write("\nHey i am the third line")
file.close()

# f = open("writing.txt",'r')
# text = f.read()
# print(text)
# f.close()

# I can aso open the file with such like that in this way i whave no need of closing the file
f = open("Writing.txt",'r')
with open("Writing.txt",'r'):
    text = f.read()
    print(text)
