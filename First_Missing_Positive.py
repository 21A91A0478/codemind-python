n = int(input())
l = list(map(int,input().split()))
a = []
for i in l:
    if i >= 0:
        a.append(i)
for i in range(1,max(a)+2):
    if i not in a:
        print(i)
        break