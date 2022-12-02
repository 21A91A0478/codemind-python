N=int(input())
n=list(map(int,input().split()))
for i in n:
    rev=0
    while i:
        d=i%10
        rev=rev*10+d
        i=i//10
    print(rev,end=' ')