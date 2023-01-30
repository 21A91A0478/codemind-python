N=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i%2!=0:
        a.append(i)
for j in a:
    if l.index(j)%2!=0:
        b.append(l.index(j))
if len(a)==len(b):
    print('True')
else:
    print('False')