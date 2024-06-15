# String Methods
# Strings are immutable and cannot be changed but the methods
# make the copy of that existing string
# Methods
str1 = "EACODE EAHUB SIMPLETOCODE"
# 1. upper() This will change the string in upper case
print(str1.upper())
# 2. lower() This will change the string in lower case
print(str1.lower())
# 3. rstrip() This will remove the trailing character e.g !
str2 = "EACODE!!!!"
print(str2.rstrip("!"))
# 4. replace() This will replace the selected part of string
print(str1.replace("EACODE","EAHUB"))
# 5. split() This will convert elements of string into list.
print(str1.split())