N,M=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
b=[]
for i in l1:
    if i in l2 and i not in a:
        a.append(i)
for j in l2:
    if j in l1 and j not in b:
        b.append(j)
print(len(a))