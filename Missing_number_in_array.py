for i in range(int(input())):
    N = int(input())
    l = list(map(int,input().split()))
    for i in range(1,N+1):
        if i not in l:
            print(i)