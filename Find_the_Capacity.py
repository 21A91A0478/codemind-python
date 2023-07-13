t, s, se = map(int,input().split())
r = 2*t*s*se*512
re = r//1024
print(f"{re}KB")