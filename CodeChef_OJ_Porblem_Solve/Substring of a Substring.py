for _ in range(int(input())):
    s = str(input())
    c = 0
    res = 0
    for i in range(len(s)):
        if s[i] != s[0] and s[i] != s[len(s)-1]:
            c += 1
        else:
            c = 0
        res = max(res,c)
    if res == 0:
        print(-1)
    else:
        print(res)
