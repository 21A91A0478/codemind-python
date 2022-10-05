T=int(input())
for i in range(T):
    n=int(input())
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    if(temp==rev):
        print('True')
    else:
        print('False')