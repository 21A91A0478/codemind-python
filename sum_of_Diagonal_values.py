r, c = map(int,input().split())
mat = []
for i in range(r):
    inner_list = list(map(int,input().split()))
    mat.append(inner_list)

l = []
for i in range(r):
    for j in range(c):
        if i==j:
            l.append(mat[i][j])
        elif i+j == r-1:
            l.append(mat[i][j])
print(sum(l))