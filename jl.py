D=["a","e","i","o","u","A","E","I","O","U"]
K=int(input())
M=0
H=[]
for p in range(K):
	b=input()
	for p in b:
		if p in D:
			M+=1
	H.append([b,M])
	M=0
H.sort(key=lambda x:x[1],reverse=True)	
for p in range(K):
    print(H[p][0])
