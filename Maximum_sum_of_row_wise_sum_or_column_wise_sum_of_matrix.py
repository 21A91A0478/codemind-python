n, m = map(int,input().split())
mat = []
for i in range(n):
    elements = list(map(int,input().split()))
    mat.append(elements)
l = []
for i in range(n):
    s = 0
    for j in range(m):
        s += mat[i][j]
    l.append(s)
print(max(l))