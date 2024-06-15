# LIST COMPREHENSION

lst = [i for i in range(10)]
print(lst)
print(len(lst))

# as of my choice i can put the condition as i want the numbers in my list

lst2 = [i*i for i in range(10)]
print(lst2)
print(len(lst2))

# I f i want only the even numbers in my list so

lsteven = [i for i in range(10) if i%2==0]
print(lsteven)

# if i wanna store the odd numbers in my list i an do this
lstodd = [i for i in range(10) if i%2!=0]
print(lstodd)
print(len(lstodd))