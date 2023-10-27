# Exercise 4 : solution
# create secret code language.

coding = True
st = input("Enter any string : ")
words = st.split(" ")

if coding:
    nwords = []
    for word in words:
        if len(st) >= 3:
            r1 = "ghw"
            r2 = "kfs"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("The decoded string = ", " ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(st) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("The encoded string = ", " ".join(nwords))
