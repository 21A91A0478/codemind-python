r, c = map(int,input().split())
mat = []
for i in range(r):
    elements = list(map(int,input().split()))
    mat.append(elements)
s = 0
for i in range(r):
    for j in range(c):
        s += mat[i][j]
print(s)