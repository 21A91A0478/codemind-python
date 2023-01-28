n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
c=0
for j in a:
    c=c+j
print(c)