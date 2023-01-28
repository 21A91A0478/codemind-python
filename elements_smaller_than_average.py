N=int(input())
l=list(map(int,input().split()))
avg=sum(l)/N
c=0
for i in l:
    if i<=int(avg):
        c=c+1
print(c)