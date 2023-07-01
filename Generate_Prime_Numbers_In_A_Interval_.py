# generate in range
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
m = int(input())
for i in range(n, m):
    if prime(i):
        print(i)