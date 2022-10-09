def reverse(num):
    s=0
    while num:
        r=num%10
        s=s*10+r
        num=num//10
    return s
n=int(input())
s=0
if n<0:
    s=1
n=abs(n)
n=reverse(n)
if s==1:
    print(-n)
else:
    print(n)