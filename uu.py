vi=int(input())
d=list(map(int,input().split()))
for y in range(len(d)-1):
   if(d[y]>d[y+1]):
      print(y)
