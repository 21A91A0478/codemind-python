import math
t=int(input())
for i in range(0,t+1):
    n=int(input())
    r=math.sqrt(n)
    if(r==int(r)):
        print('True')
    else:
        print('False')
