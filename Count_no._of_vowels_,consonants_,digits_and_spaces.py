s=input()
v='aeiou'
d='0123456789'
V=C=W=D=0
for i in s:
    if i in v:
        V=V+1
    elif i==' ':
        W=W+1
    elif i in d:
        D=D+1
    else:
        C=C+1
print('Vowels:'+' ' + str(V))
print('Consonants:'+' '+str(C))
print('Digits:'+' '+str(D))
print('White spaces:'+' '+str(W))