n=input()
v='aeiou'
c=0
a=[]
for i in n:
    if i in v:
        c=c+1
        a.append(c)
    else:
        c=0
print(max(a))