n = int(input())
l = list(map(int,input().split()))
t = int(input())
r = l[::-1]
if t not in l:
    print(-1, -1)
else:
    f = l.index(t)
    e = n - (r.index(t)+1)
    print(f, e)
    