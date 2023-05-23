n = int(input())
l = list(map(int,input().split()))
lst = []
for i in l:
    lst.append(i*i)
s = sorted(lst)
print(*s)