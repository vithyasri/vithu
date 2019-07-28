J,L=map(int,input().split())
R=[]
M=""
U=list(map(int,input().split()))
for p in range(0,L):
	U.append(U[0])
	U.remove(U[0])
for p in U:
   
        M=M+str(p)+" "
print(M.strip())
