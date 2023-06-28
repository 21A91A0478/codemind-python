r, c = map(int,input().split())
mat = [list(map(int,input().split()))for i in range(r)]
s = 0
for i in mat:
    c = i.copy()
    c.sort()
    if i == c or i == c[::-1]:
        s += 1
print(s)