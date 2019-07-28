D=int(input())
S=input()
H=[]
for j in S:
	H.append(S.count(j))
for j in range(0,len(H)):
	K=min(H)
	if H[j]==K:
		print (S[j])
		break
