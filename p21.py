n1,m1=map(int,input().split())
n2,m2=map(int,input().split())
n3,m3=map(int,input().split())
if n1==m1 and n2==m2 and n3==m3:
	print("yes")
elif n1==n2 and n1==n3:
	print("yes")
elif m1==m2 and m1==m3:
	print("yes")
else:
	print("no")
