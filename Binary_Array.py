n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i==0 or i==1:
        a.append(i)
if len(a)==len(l):
    print('True')
else:
    print('False')