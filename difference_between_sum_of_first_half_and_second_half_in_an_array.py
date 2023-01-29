N=int(input())
l=list(map(int,input().split()))
h=N//2
a=[]
b=[]
for i in range(N):
    if i<h:
        a.append(l[i])
    else:
        b.append(l[i])
f=0
s=0
for j in a:
    f=f+j
for k in b:
    s=s+k
print(abs(f-s))