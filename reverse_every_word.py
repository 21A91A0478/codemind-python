n=input()
l=n.split()
a=[]
for i in l:
    d=i[::-1]
    a.append(d)
b=' '.join(a)
print(b)
    