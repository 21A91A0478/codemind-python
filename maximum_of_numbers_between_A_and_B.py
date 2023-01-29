N=int(input())
l=list(map(int,input().split()))
A,B=map(int,input().split())
a=[]
for i in l:
    if i<=B and i>=A:
        a.append(i)
if not a:
    print('-1')
else:
    print(max(a))