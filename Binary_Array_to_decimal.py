n = int(input())
l = list(map(int,input().split()))
s = ''
for i in l:
    s += str(i)
r = int(s, 2)
print(r)