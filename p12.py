F,D=map(int,input().split())

K=[]
M=list(map(int,input().split()))
K=(M[-D:]+M[:-D])
for p in range(0,len(K)):
	print(K[p],end=" ")
