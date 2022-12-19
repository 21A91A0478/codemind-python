T=int(input())
for i in range(T):
    s=0
    L,R=map(int,input().split())
    for j in range(L,R+1):
        l=j%10
        if l==2 or l==3 or l==9:
            s=s+1
    print(s)