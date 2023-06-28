r, c = map(int,input().split())
mat = []
for i in range(r):
    elements = list(map(int,input().split()))
    mat.append(elements)
s = 0
for i in range(1, r-1):
    for j in range(1, c-1):
        s += mat[i][j]
print(s)