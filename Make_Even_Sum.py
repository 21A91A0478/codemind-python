n=int(input())
a=list(map(int,input().split()))
l=len(a)
s=0
for i in range(l):
    s=s+a[i]
if s%2==0:
    print("1")
else:
    print("0")