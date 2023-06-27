r, c = map(int,input().split())
mat = []
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)

m = [[0 for i in range(r)] for j in range(c)]
for i in range(r):
    for j in range(c):
        m[j][i] = mat[i][j]

l = []
for i in range(c):
    s = 0
    for j in range(r):
        s += m[i][j]
    l.append(s)
print(*l)