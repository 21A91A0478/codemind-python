n=input()
v='aeiou'
l=len(v)
a=[]
for i in range(l):
    for j in n:
        if v[i] in j:
            break
    else:
        a.append(v[i])
if len(a)!=0:
    print(' '.join(a))
else:
    print('0')
