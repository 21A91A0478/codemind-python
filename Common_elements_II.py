N,M=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
b=[]
for i in l1:
    if i not in l2:
        a.append(i)
for j in l2:
    if j not in l1:
        b.append(j)
print(*(a+b))