N = int(input())
lst = list(map(int,input().split()))
l = len(lst)//2
l1 = lst[:l]
l2 = (lst[l:])[::-1]
l3 = l2 + l1
for i in l3:
    print(i,end=" ")