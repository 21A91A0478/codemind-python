n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l1 = []
l2 = []
for i in a:
    if i not in b and i not in l1:
        l1.append(i)
for i in b:
    if i not in a and i not in l2:
        l2.append(i)
print(len(l1)+len(l2))