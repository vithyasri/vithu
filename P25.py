D=input()
V=input().split()
Y=[]
for j in V:
	Y.append(j)
Y.sort()
Y.sort(key=len)
for j in Y:
	print(j,end=" ")
	
