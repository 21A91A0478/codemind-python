n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if l.count(i) == i and i not in a:
        a.append(i)
if a:
    print(*a)
else:
    print(-1)