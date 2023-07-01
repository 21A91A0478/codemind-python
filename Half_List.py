n = int(input())
l = list(map(int,input().split()))
h = n//2
h1 = l[:h]
h2 = l[h:][::-1]
print(*(h2+h1))