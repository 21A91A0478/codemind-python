n = int(input())
l = list(map(int,input().split()))
a = []
while len(l)>2:
    a.append(l[0])
    a.append(l[-1])
    l.pop(0)
    l.pop(-1)
if len(l)==1:
    a.append(l[0])
    a.append(0)
elif len(l)==2:
    a.append(l[0])
    a.append(l[-1])
print(*a)