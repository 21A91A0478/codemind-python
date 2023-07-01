#Circular Prime
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

num = int(input())
r = 0
temp = num
while temp:
    d = temp % 10
    temp = temp // 10
    r = r * 10 + d
if prime(num)==1 and prime(r)==1:
    print("circular prime")
elif prime(num)==1 and prime(r)==0:
    print("prime but not a circular prime")
else:
    print("not prime")