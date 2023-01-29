N=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if i==k or i<=k:
        c=c+i
    else:
        break
print(c)