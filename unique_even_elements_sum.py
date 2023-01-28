N=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i%2==0 and i not in a:
        a.append(i)
c=0
for j in a:
    if j%2==0:
        c=c+j
print(c)