n = int(input())
mat1 = [list(map(int,input().split())) for i in range(n)]
mat2 = [list(map(int,input().split())) for i in range(n)]
mat3 = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(abs(mat1[i][j]-mat2[i][j]))
    mat3.append(l)
for i in mat3:
    print(*i)