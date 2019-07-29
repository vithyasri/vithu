D=input()
L=""
A=""
for j in D:
    if j=="V":
        A="L"
        L=L+A
    elif j=="B":
        A="b"
        L=L+A
    elif j=="z":
        A="c"
        L=L+A
    elif j=="Y":
        A="B"
        L=L+A
    elif j=="Z":
        A="C"
        L=L+A
    elif j=="X":
        A=="A"
    else:
        A=ord(j)+3
        L=L+str(chr(A))
	
print(L)
		
