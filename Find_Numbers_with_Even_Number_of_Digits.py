n = int(input())
l = list(map(int,input().split()))
s = list(map(str,l))
c = 0
for i in s:
    if len(i) % 2 == 0:
        c += 1
print(c)