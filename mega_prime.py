#Mega Prime
def prime(n):
    if n < 2:
        return False
    c = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            c += 1
    if c == 0:
        return True
    return False

n = int(input())
l = []
temp = n
while temp:
    d = temp % 10
    temp = temp // 10
    l.append(d)
c = 0
for i in l:
    if prime(i)==True:
        c += 1
if c==len(l) and prime(n)==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")