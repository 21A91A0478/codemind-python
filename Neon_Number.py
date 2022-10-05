n=int(input())
s=0
temp=n**2
while temp>0:
    r=temp%10
    s=s+r
    temp=temp//10
if(n==s):
    print('Neon Number')
else:
    print('Not Neon Number')