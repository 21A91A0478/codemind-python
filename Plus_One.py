n = int(input())
l = list(map(int,input().split()))
num = ''
for i in l:
    num += str(i)
num = int(num) + 1
lst = list(str(num))
print(*lst)