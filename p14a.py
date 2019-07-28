D=int(input())
P=input()
N=["a","e","i","o","u","A","E","I","O","U"]
K=""
for p in P:
	if p not in N:
		K=K+p
print(K[::-1])
