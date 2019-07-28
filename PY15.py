G=input()
X=[]
for j in G:
    X.append(G.count(j))
for j in range(0,len(X)):
    N=max(X)
    if X[j]==N:
        print(G[j])
        break
