C,J=map(str,input().split())
for p in range(len(C)):
    if(C.count(C[p])==J.count(J[p])):
        print("yes")
        break
    else:
        print("no")
        break
