def pal(i):
    rev=0
    temp=i
    while i:
        d=i%10
        rev=rev*10+d
        i=i//10
    if temp==rev:
        return True
    else:
        return False
        

n=int(input())
N=list(map(int,input().split()))
c=0
for i in N:
    if pal(i)==True:
        c=c+1
print(c)