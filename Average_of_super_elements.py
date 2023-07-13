n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if l.count(i) == i:
        a.append(i)
if not a:
    print(-1)
else:
    print(format(len(a)/len(set(a)),".2f"))