n=int(input())
s=str(n)
a=[]
for i in range(len(s)):
    if int(s[i])%2!=0:
        d=(int(s[i]))**2
        a.append(d)
b=[str(item) for item in a]
print(''.join(b))