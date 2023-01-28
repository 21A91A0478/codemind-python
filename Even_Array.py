N=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0 or i==0:
        e.append(i)
    else:
        o.append(i)
if not o:
    print('True')
else:
    print('False')