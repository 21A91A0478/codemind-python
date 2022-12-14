n=input()
s=n.split()
l=len(s)
a=[]
for i in range(l):
    if i%2==0:
        a.append(s[i][::-1])
    else:
        a.append(s[i])
print(' '.join(a))