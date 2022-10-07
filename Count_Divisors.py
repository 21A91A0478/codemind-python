i,r,k=map(int,input().split())
s=0
for n in range(i,r+1):
    if(n%k==0):
        s=s+1
print(s)