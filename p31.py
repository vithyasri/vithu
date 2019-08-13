D=input()
V=0
L=0
for j in range(len(D)):
    if D[j]=="(":
        V=V+1
    if D[j]==")":
        L=L+1
if V==L:
    print("yes")
else:
    print("no")
