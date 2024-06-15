# BREAK AND CONTINUE STATEMENTS
# BREAK MEANS TO END THE LOOP AND COME OUTSIDE
# CONTINUE MEANS TO END THE ITERATION AND COME OUTSIDE

for i in range(12):
    print("5 X ",i, " = ", 5*i)
    if(i == 10):
        break
print("Loop ended.")


for i in range(12):
    if(i==10):
        break;
    print("5 X ",i+1," = ",5*(i+1))

# CONTINUE SY SKIP HOTI HAI ITERATION

for i in range(12):
    if(i==10):
        print("The iteration miss.")
        continue                       # 10 k lie nhi execute hoga ye
    print("5 X ",i," = ",5*i)
