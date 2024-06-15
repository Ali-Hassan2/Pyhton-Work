# DICTONARIE METHODS IN PYTHON
# 1. To make the combinition of two dictonaries
cmp1 = {111:23, 112:56, 113:76}
cmp2 = {222:45, 223:97}
cmp1.update(cmp2)
print(cmp1)
# 2. clear() to remove the items in the dict.
print(cmp2)
cmp2.clear()
print(cmp2)
# 3. Pop() to remove the selecte value
print(cmp1.pop(111))
# 4. del dictonary_name
del cmp2
# 5. popitem() to remove the last item
print(cmp1.popitem())
if 112 in cmp1:
    print("Yes present.")
else:
    print("No not present.")




