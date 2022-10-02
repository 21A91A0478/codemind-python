n=int(input())
rev=0
while n:
    s=n%10
    rev=rev*10+s
    n=n//10
print(rev)