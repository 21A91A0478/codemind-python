def prime(num):
    count=0
    for k in range(1,num+1):
        if num%k==0:
            count=count+1
    if count==2:
        return 1
    else:
        return 0


n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
s=0
a=[]
while n:
    d=n%10
    n=n//10
    a.append(d)
for j in a:
    cc=0
    if prime(j)==1:
        cc=cc+1
if c==2 and cc==1:
    print('Mega Prime')
else:
    print('Not Mega Prime')