n = int(input())
l = list(map(int,input().split()))
s = set(l)
c = 0
for i in s:
    if i == l.count(i):
        c += 1
print(c)