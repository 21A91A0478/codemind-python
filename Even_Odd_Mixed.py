n=input()
l=list(n)
a=[]
b=[]
for i in l:
    if int(i)%2==0:
        a.append(i)
    else:
        b.append(i)
if len(a)==len(l):
    print('Even')
elif len(b)==len(l):
    print('Odd')
else:
    print('Mixed')