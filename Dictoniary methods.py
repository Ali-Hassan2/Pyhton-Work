# Dictonarys method
# employee ids and there performance number

# 1. dict1.update(dict2)

company1 = {111: 56, 112: 67, 113: 87}
company2 = {222: 47, 223:97}

company1.update(company2)

print(company1)

# 2. clear() remove the items in the dictonary

company2.clear()
print(company2)

# 3. Pop the selected item
company1.pop(111)
print(company1)

# 4. popitem() to remove the last item in the dictonary.
company1.popitem();
print(company1)

# 5. del dictonary_name
del company2

# print(company2)

if 112 in company1:
    print("yes")
else:
    print("no")

