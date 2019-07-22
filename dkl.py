D=input()
K=''
L=''
for p in D:
  if(p=='a' or p=='e' or p=='i' or p=='o' or p=='u' or p=='A' or p=='E' or p=='I' or p=='O' or p=='U'):
    K=K+p
  else:
    L=L+p
print(K+L)
