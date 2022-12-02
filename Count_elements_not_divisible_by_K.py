N,K=map(int,input().split())
n=list(map(int,input().split()))
c=0
for i in n:
    if i%K!=0:
        c=c+1
print(c)