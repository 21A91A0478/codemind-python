n = int(input())
a = list(map(int,input().split()))
l = len(a) // 2
a1 = a[:l]
a2 = a[l:]
a3 = []
for i in range(max(len(a1),len(a2))):
    if i < len(a1):
        a3.append(a1[i])
    if i < len(a2):
        a3.append(a2[i])
for i in a3:
    print(i,end=' ')