import math
D,V=map(int,input().split())
t=0
for j in range(D,V+1):
    Y=math.sqrt(j)
    if(Y-math.floor(Y)==0):
        t=t+1
print(t)
