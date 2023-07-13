n = int(input())
k = n
while k:
    if k==1:
        print("Ugly Number")
        break
    if k%2==0:
        k = k//2
    elif k%3==0:
        k = k//3
    elif k%5==0:
        k = k//5
    else:
        print("Not Ugly Number")
        break