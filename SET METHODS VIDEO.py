# STRING METHODS IN PYTHON

s1 =  {1,2,3,4,5,7,8}
s2 = {6,7,8}

# 1. union

# print(s1.union(s2))
# # Intersection
# print(s1.intersection(s2))
#
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))

s1.add(10)
print(s1)

s1.remove(2)
print(s1)

s1.discard(3)
print(s1)

s1.pop()
print(s1)

del s1

s2.clear()
print(s2)

s2.add(2)
print(s2)

if 2 in s2:
    print("YES PRESENT.")
else:
    print("NO.")



