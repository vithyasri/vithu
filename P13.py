J=int(input())
D=0
while J>0:
	P=J%10
	D=D+(P**2)
	J=J//10
print(D)
