D,K=map(int,input().split())
for j in range(2,10000):
	if j%D==0 and j%K==0:
		print(j)
		break
