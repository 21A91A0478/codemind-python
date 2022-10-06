num=int(input())
while num>9:
    rem=num%10
    quo=num//10
    num=rem+quo
if num<9:
    print(num)