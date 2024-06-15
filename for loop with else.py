
for i in range(6):
     print(i)
else:
 print("There is no i")

 # Else codition with loop means wwhen the loop ends or it does not break when it complete to iterate then the
 # else condition will be executed.
for i in range(6):
    print(i)
    if i == 4:
         break
else:
    print("There is no 1.")
    # In this case there is the break means the loop not completely execute so else condtio will not execute.
#  same case is with the while loop
count = 0
while count < 7:
    print(count)
    count = count + 1
else:
    print("i ended.")

# second case in which else will not execute
count2 = 1
while count2 <= 10:
    print(count2)
    if count2 == 6:
        break;
    count2 = count2 + 1
else:
    print("There is no i.")