# 1. Append()

list = [1,2,3,4,5]

list.append(7)
print(list)
list.append(8)
print(list)

# 2. Sort()
# In ascending order
s = [5,3,2,1]
s.sort()
print(s)

# In descendign order
d = [1,2,3,4,5]
d.sort(reverse=True)
print(d)

# 3. Reverse()

r = [1,3,5,4,6]
r.reverse()
print(r)

# 4. count
c = [1,2,2,3,4,2]
print(c.count(2),"times.")
# Return 3 times
# 5. copy()
l = [1,2,3,4,5,6]
m = l.copy()
m[0] = 4
print(m)
print("This is unchanged.",l)

# I can also merge the lists as
list1 = [1,2,3,4]
list2 = [5,6]
list3 = list1 + list2
print(list3)

# 4. insert insert(which index, which value)

i = [1,2,3,4,5]
i.insert(2,44)
print(i)

# 5. extend()
l2  = [55,66,77,88]
m = [1000,5000,60000]
l2.extend(m)
print(l2)
