N=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(N):
    a.append(l[i])
if N%2!=0:
    a.append('0')
print(*(a))