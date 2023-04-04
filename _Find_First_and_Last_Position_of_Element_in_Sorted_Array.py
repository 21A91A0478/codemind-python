n = int(input())
l = list(map(int,input().split()))
num = int(input())
a = []
b = [-1,-1]
for i in range(len(l)):
    if l[i] == num:
        a.append(i)
if len(a) != 0:
    for i in a:
        print(i,end=' ')
else:
    for i in b:
        print(i,end=' ')