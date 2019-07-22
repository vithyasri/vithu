D=int(input())
K=list(map(int,input().split()))
H=0
for J in K:
    if J<0:
        H=H+J
print(H)
