def is_prime(n):
    if n==1:
        return False
    s = int(n**0.5)
    for i in range(2,s+1):
        if n%i == 0:
            return False
    return True
n = int(input())
m = int(input())
c = 0
for j in range(n,m+1):
    if is_prime(j):
        c+=1
print(c)