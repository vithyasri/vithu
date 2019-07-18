G6,I7=map(int,input().split())
char=input().split()
P=[]
for i in char:
	if(int(i)%2!=0):
		P.append(i)
print(P[I7-1])
