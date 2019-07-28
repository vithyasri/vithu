D=int(input())
K=[]
flag=1
X=[]
N=""
for J in range(2,D+1):
    for p in range(2,D+1):
        if J*p==D:
            K.append(J)
for J in K:
    for p in range(2,J):
        if J%p==0:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        N=N+str(J)+" "
print(N.strip())
