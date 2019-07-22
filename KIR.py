def vithya(D):
    if(D<=1):
        return 1
    Y=0
    for i in range(D):
        Y=Y+vithya(i)*vithya(D-i-1)
    return Y

G=int(input())
for p in range(G):
    print(vithya(p),end=" ")
