import math
def perfectsq(x):
    s=int(math.sqrt(x))
    return s*s==x

n=int(input())
temp1=(5*(n*n)+4)
temp2=(5*(n*n)-4)
if perfectsq(temp1)or perfectsq(temp2):
    print('True')
else:
    print('False')