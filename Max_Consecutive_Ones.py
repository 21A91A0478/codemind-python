n = int(input())
l = list(map(int,input().split()))
c = 0
a = []
for i in l:
    if i == 1:
        c += 1
    else:
        c = 0
    a.append(c)
print(max(a))