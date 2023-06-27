r, c = map(int,input().split())
mat = []
for i in range(r):
    elements = list(map(int,input().split()))
    mat.append(elements)
es = 0
os = 0
for i in range(r):
    for j in range(c):
        l = mat[i][j]
        if l%2:
            os += l
        else:
            es += l
print(es, os)