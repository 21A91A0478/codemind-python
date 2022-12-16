s=input()
a=[]
v='aeiouAEIOU'
for i in s:
    if i in v and i not in a:
        a.append(i)
if a:
    print(' '.join(a))
else:
    print('-1')