def hpy(n):
    s=0
    while n>0:
        r=n%10
        s=s+r*r
        n=n//10
    return s

n=int(input())
res=n
while res>9:
    res=hpy(res)
if res==1 or res==7:
    print('True')
else:
    print('False')
