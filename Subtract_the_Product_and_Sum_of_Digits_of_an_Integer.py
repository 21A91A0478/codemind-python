n=int(input())
s=0
p=1
while n>0:
    temp=n%10
    s=s+temp
    p=p*temp
    n=n//10
print(p-s)