n = int(input())
l = list(map(int,input().split()))
l.sort()
a = []
for i in l:
    a.append(i*i)
a.sort()
for i in a:
    print(i,end=' ')
