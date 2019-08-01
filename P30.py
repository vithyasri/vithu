D,N,M=map(str,input().split())
D=list(D)
N=list(N)
M=int(M)
count=0
for j in range(0,len(D)):
        if(D[j]!=N[j]):
            count=count+1
if(count==M):
    print("yes")
else:
    print("no")
