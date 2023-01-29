N=int(input())
l=list(map(int,input().split()))
A,B=map(int,input().split())
a=[]
for i in l:
    if i<=B and i>=A:
        a.append(i)
c=0
for j in a:
    c=c+j
print(c)
        