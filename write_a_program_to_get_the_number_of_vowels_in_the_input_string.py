s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c=c+1
if c:
    print(c)
else:
    print('0')