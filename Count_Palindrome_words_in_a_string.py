def pal(n):
    if n == n[::-1]:
        return 1
    else:
        return 0


s = input().lower()
l = s.split(' ')
c = 0
for i in l:
    if pal(i) == 1:
        c += 1
print(c)
