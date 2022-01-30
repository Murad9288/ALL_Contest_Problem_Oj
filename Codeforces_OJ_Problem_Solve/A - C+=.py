for _ in range(int(input())):
    a,b,n = map(int,input().split())
    c = 0
    while max(a,b) <= n:
        c += 1
        if a > b:
            b += a
        else:
            a += b
    print(c)
