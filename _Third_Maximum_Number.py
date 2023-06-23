n = int(input())
a = list(map(int,input().split()))
s = set(a)
b = sorted(s, reverse=True)
if len(b) >= 3:
    print(b[2])
else:
    print(max(b))