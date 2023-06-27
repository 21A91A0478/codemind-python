r, c = map(int,input().split())
mat = []
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)

l = []
for i in range(c):
    s = 0
    for j in range(r):
        s += mat[j][i]
    l.append(s)
print(*l)