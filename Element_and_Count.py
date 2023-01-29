N=int(input())
l=list(map(int,input().split()))
a=[]
c=[]
for k in l:
    if k not in c:
        c.append(k)
for i in c:
    a.append(l.count(i))
b=(item for sublist in zip(c,a)for item in sublist)
print(*b)