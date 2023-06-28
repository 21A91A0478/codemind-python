s1 = input().lower()
s2 = input().lower()
l = []
s3 = s1.split(' ')
s4 = s2.split(' ')
for i in s4:
    if i in s3:
        l.append(i)
print(*l)