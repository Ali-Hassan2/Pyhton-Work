# 6. Captalize()

line = "follow to eacode"
print(line.capitalize())

# 7. Center() This will align the string in the center with the parameters passed by the user
print(len(line))
print(line.center(50))
print(len(line.center((50))))

# 8. Count() Tells that the alphabet how many times comes to in the string

a = "aaaaaaa"
print(a.count("a"))

# 9. endwith() Tells that wether the given string ends with given value or not
x = "Welcome to EACODE!"
print(x.endswith("!"))

# 10. find() Finds the given word in the string and returns the index
y = "Welcome to EACODE"
print(y.find("to"))

# 11. isalnum() Only trues if the string is in A-Z or a-z and 0-9
s = "WelcomeToEaCode"
print(s.isalnum())

# 12. isalpha() Only trues if the string is A-Z or a-z
s1 = "WelcomeToEaCode"
print(s.isalpha())
s2 = "WelcomeToEacode22"
print(s2.isalpha())

# 13. islower() returns true only if all the letters are lower
s3 = "welcometoeacode"
print(s3.islower())
# 14. isupper() return true value only if all the letters are upper
s4 = "WELCOMETOEACODE"
print(s4.isupper())
# 15. isprintable() returns true if not a escape sequence is mixed
s5  = "Hey Welcome To The EaCode."
print(s5.isprintable())
s6 = "hey welcome to the eacode\n"
print(s6.isprintable())

# 16. istitle() returns true only if the evey first letter of the word in the string is capital

# Worl Health Organiztion

s7 = "World Health Organiztion"
print(s7.istitle())
s8 = "world Health organization"
print(s8.istitle())

# 17. title() change the string in the title

s9 = "world health organiztion"
print(s9.title())