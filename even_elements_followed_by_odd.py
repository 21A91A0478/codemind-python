N=int(input())
l=list(map(int,input().split()))
o=[]
e=[]
for i in l:
    if i%2!=0:
        o.append(i)
    else:
        e.append(i)
print(*(e+o))
        