
r, c = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(r)]
l = []
for j in range(c):
    lst = []
    for i in range(r):
        lst.append(mat[i][j])
    l.append(lst)
s = 0
for i in l:
    c = i.copy()
    c.sort()
    if i == c :
        s += 1
print(s)