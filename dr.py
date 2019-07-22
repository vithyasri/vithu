
D,P=map(int,input().split())
K=[]
for p in range(D,P+1):
    if(p>1):
       for k in range(2,p):
           if(p%k==0):
               break
       else:
          K.append(p)
print(len(K))
