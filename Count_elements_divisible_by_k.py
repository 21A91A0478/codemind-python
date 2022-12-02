n,k=map(int,input().split())
N=list(map(int,input().split()))
c=0
for i in N:
    if i%k==0:
        c=c+1
print(c)