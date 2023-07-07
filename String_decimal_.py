for _ in range(int(input())):
    s = input()
    c = 0
    for i in s:
        if i not in "0123456789":
            c += 1
    if c:
        print("False")
    else:
        print("True")