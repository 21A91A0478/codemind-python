n = int(input())
l = list(map(int,input().split()))
s = set(l)
lst = []
for i in s:
    if i == l.count(i):
        lst.append(i)
if lst:
    print(min(lst),max(lst))
else:
    print('-1')