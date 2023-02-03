n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    while i:
        d=i%10
        i=i//10
        a.append(d)
print(sum(a))