n = int(input())
l = list(map(int,input().split()))
s = ''
for i in l:
    s += str(i)
r = s[::-1]
a = []
for i in range(len(r)):
    if r[i] == '1':
        a.append(2 ** i)
print(sum(a))