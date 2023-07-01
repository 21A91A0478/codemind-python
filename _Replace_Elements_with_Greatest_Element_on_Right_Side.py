n = int(input())
l = list(map(int,input().split()))
lst = []
m = []
while len(l)>1:
    for i in range(1, len(l)):
        m.append(l[i])
    ma = max(m)
    lst.append(ma)
    m = []
    l.pop(0)
if len(l) == 1:
    lst.append(-1)
print(*lst)