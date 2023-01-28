N=int(input())
l=list(map(int,input().split()))
A,B=map(int,input().split())
a=[]
b=[]
for i in l:
    if i<=B and i>=A:
        a.append(i)
    else:
        b.append(i)
if not b:
    print('-1')
else:
    print(max(b))
