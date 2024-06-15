
str = input("Enter the message: ")
words = str.split(" ")
coding = False
if coding:
    nword = []
    for word in words:
        if(len(word) >= 3):
            random1 = "dsf"
            random2 = "hyk"

            string_new = random1 + word[1:] + word[0] + random2
            nword.append(string_new)
        else:
            nword.append(word[::-1])  # reverse the string
    print(" ".join(nword))

else:
    nwords = []
    for word in words:
        if(len(word) >= 3):
            stnew = word[3: -3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))


