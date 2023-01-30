n=int(input())
f=0
s=1
for i in range(n):
    print(f,end=' ')
    temp=f
    f=s
    s=temp+f
    