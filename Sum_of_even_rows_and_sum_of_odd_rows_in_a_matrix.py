r, c = map(int,input().split())
a = []
for i in range(r):
    elements = list(map(int,input().split()))
    a.append(elements)
ec = 0
oc = 0
for i in range(r):
    for j in range(c):
        if i==0 or i%2==0:
            ec += a[i][j]
        else:
            oc += a[i][j]
print(ec, oc)
            