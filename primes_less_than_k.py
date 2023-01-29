def prime(n):
    c=0
    for j in range(1,n+1):
        if n%j==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0

N=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if i<=k:
        if prime(i)==1:
            a.append(i)
print(len(a))