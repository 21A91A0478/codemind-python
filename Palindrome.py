n=int(input())
rev=0
m=n
while m>0:
    temp=m%10
    m=m//10
    rev=rev*10+temp
if rev==n:
    print('True')
else:
    print('False')