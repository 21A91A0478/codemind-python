N = int(input())
lst = list(map(int,input().split()))
n = int(input())
l = len(lst) - n
s = lst[l:] + lst[:l]
for i in s:
    print(i,end=' ')