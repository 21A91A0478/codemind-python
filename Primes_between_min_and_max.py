def prime(n):
    if n < 2:
        return False
    c = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
l = list(map(int,input().split()))
mi = l.index(min(l))
ma = l.index(max(l))
s = 0
if mi>ma:
    for i in range(ma,mi+1):
        if prime(l[i]):
            s += 1
else:
    for i in range(mi,ma+1):
        if prime(l[i]):
            s += 1
print(s)