# Set methods in the Python

# 1. Union.

s1 = {1,2,3,4,5}
s2 = {6,7,8,4,5}

s3 = s1.union(s2)
print("The union of s1 and s2 is: ",s3)

# 2. Intersection

s4 = s1.intersection(s2)
print("The intersection of s1 and s2 is: ",s4)

# 3. Disjoint
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

# 4. add the element

s1.add(9)
print(s1)

s1.remove(3)
print(s1)
s1.discard(1)
print(s1)

del s1

s2.clear()
print(s2)

s2.add(2)
print(s2)

if 2 in s2:
    print("Yes present.")
else:
    print("NO.")

