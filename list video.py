# LIST OPERATIONS
# 1. Append() this will add at the last
list = [1,2,3,4,5]
list.append(6)
print(list)
# 2. sort() in ascending for descending
#    sort(reverse = True)
s = [4,2,5,6]
s.sort()
print(s)
# in descending order
s.sort(reverse= True)
print(s)
# 3. Reverse() This will reverse the list
list.reverse()
print(list)
# 4. count() count and tell the existence
c = [1,1,2,2,2,4,5,6]
print(c.count(1),"times.")
print(c.count(2),"times.")
# 5. copy() will make the copy of the list
m = list.copy()
print(m)
# 6. insert() will insert at the given index
list.insert(3,66)
print(list)
# 7 . extend() will extend the list
n = [1000,45555,33333]
list.extend(n)
print(list)