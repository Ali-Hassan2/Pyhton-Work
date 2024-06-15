

list = [12,17,14,15,11,22,14,15,16,10]

# index = 0
# for lis in list:
#     print(lis)
#     # Checking the index and printing the messgae at the highest marks
#     if index == 5:
#         print("These are the maximum numbers attained by a student.")
#     index = index + 1

# I can do the same thing by the enumeration function in such a way.

for index, lis in enumerate(list):
    print(lis)

    if index == 5:
        print("Highest marks ever attained by a brilliant student.")

        # So we can trigger the index by this
        # so there is also something else as the index starts from the 0 but we can start it from 1 as the following
for ind, li in enumerate(list,start=1):
    print(li)
    if ind == 6:
        print("This is the start faciltity.")
