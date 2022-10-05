def palindrome(n):
    temp=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==temp:
        return True
    else:
        return False

n=int(input())
print(palindrome(n))