n = int(input())
l = list(map(int,input().split()))
c = 0
i = 0
j = 2
while i<n and j<n:
    if l[i]%2==0 and l[j]%2!=0 or l[i]%2!=0 and l[j]%2==0:
        c += 1
    i += 1
    j += 1
print(c)