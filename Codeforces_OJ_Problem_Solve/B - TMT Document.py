for _ in range(int(input())):
    n = int(input())
    s = str(input())[:n]
    c = 0
    res = 0
    for i in s:
        if i == "T":
            c += 1
        else:
            c -= 1
        res = n//3
        if c>res or c<0:
            break
    if c == res:
        print("YES")
    else:
        print("NO")
