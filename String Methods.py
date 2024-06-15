# String methods
# Strings are immutable and cannot be changes the methods makes a copy of the existings strings
# These methods will not change the existing string
# Methods
str = "EaCode"
# 1. Upper()
print(str.upper())
# 2. lower()
print(str.lower())
# 3. rstrip()   It will remove any trailing characters e.g !!!
str2 = "EACODE!!!!!"
print(str2.rstrip("!"))
# 4. replace() repalce the selected part of the string
print(str.replace("EaCode","EaHub"))
# 5. split() it will sppilt the elements in the string into a list
list = "EaCode EaHub SimpletoCode"
print(list.split())