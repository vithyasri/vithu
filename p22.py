D,V=map(int,input().split())
Y=min(D,V)
P=[]
for j in range(1,Y+1):
    if((D%j==0) and (V%j==0)):
        P.append(j)
print(max(P))
