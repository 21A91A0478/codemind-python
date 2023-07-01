def prime(n):
    if n < 2:
        return 0
    c = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            c += 1
    if c == 0:
        return 1
    return 0
    
n = int(input())
if prime(n):
    print("prime")
else:
    print("not a prime")