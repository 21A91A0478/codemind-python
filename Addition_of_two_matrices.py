n = int(input())
m1 = [list(map(int,input().split())) for i in range(n)]
m2 = [list(map(int,input().split())) for i in range(n)]
m3 = []
for i in range(n):
    m = []
    for j in range(n):
        m.append(m1[i][j]+m2[i][j])
    m3.append(m)
    
for i in range(n):
    for j in range(n):
        print(m3[i][j], end=' ')
    print()