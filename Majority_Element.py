n=int(input())
l=list(map(int,input().split()))
c=0
num=0
for i in l:
    counter=l.count(i)
    if counter>c:
        c=counter
        num=i
print(num)