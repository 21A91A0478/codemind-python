s1 = input().lower()
s2 = input().lower()
l1 = []
l2 = []
for i in s1:
    if i not in l1 and i.isalpha():
        l1.append(i)
for i in s2:
    if i not in l2 and i.isalpha():
        l2.append(i)
l = []
for i in l1:
    if i not in l2:
        l.append(i)
for i in l2:
    if i not in l1:
        l.append(i)
l.sort()
s = ''
for i in l:
    s += i
print(s)