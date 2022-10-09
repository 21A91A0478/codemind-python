a=int(input())
temp=a%10
while a>0:
    x=a%10
    if x>temp:
        temp=x
    a=a//10
print(temp)