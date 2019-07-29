num=list(input())
alt=[]
kill=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for p in num:
    if p=='X':
        alt.append("A")
    elif p=='Y':
        alt.append("B")
    elif p=="Z":
        alt.append("C")
    else:
        alt.append(kill[kill.index(p)+3])
print("".join(alt))
