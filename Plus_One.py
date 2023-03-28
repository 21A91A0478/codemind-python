n = int(input())
l = list(map(int,input().split()))
s = list(map(str,l))
st = ""
for i in s:
    st += i
lst = int(st) + 1
lis = list(str(lst))
e = [ eval(i) for i in lis ]
for j in e:
    print(j,end=" ")