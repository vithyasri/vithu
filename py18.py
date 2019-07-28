D=int(input())
N=[]
T=0
L="kabali"
B=sorted(L)
for j in range(D):
	G=input()
	N.append(G)
for j in N:
	if sorted(j)==B:
		T=T+1
print(T)
