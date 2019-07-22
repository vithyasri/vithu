D = input()
W = len(D)
M = []
for p in range(0,W,2):
   M.append(D[p:p+2][::-1])
print("".join(M))
