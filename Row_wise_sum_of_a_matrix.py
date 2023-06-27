r, c = map(int,input().split())
mat = []
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)

l = []
for i in range(r):
    s = 0
    for j in range(c):
        s += mat[i][j]
    l.append(s)
print(*l)