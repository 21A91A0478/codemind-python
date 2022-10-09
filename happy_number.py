def sod(n):
    s=0
    r=0
    while n>0:
        r=n%10
        s=s + r*r
        n=n//10
    return s

n=int(input())
result=n
while (result!=1 and result!=4):
    result=sod(result)
if result==1:
    print('True')
else:
    print('False')