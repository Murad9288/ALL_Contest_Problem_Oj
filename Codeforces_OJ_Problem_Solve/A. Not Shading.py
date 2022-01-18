for _ in range(int(input())):
    n,m,r,c = map(int,input().split())
    s = []
    for _ in range(n):
        s.append(str(input())[:m])
    r -= 1
    c -= 1
    sum = n-(r+m)-c
    sum -= 1
    if s[r][c] == "B":
        print(0)
        continue
    f = True
    for j in range(n):
        for k in range(m):
            if s[j][k] == "B":
                f = False
    if f:
        print(-1)
    elif s[r][c] == "W":
        b = False
        for i in range(n):
            if s[i][c] == "B":
                b = True
        for j in range(m):
            if s[r][j] == "B":
                b = True
        if not b or sum == "B":
            print(2)
        else:
            print(1)
