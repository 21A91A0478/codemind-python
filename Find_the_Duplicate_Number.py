from collections import Counter
n = int(input())
l = list(map(int,input().split()))
c = Counter(l)
d = dict(c)
m = max(d.values())
for i, j in d.items():
    if j == m:
        print(i)