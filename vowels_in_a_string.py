n=input()
v=input()
l=len(n)
for i in range(l):
    if n[i] in v:
        print('True')
        print(i)
        break
else:
    print('False')