n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if l.count(i) == 1:
        a.append(i)
if a:
    print(*a)
else:
    print('-1')