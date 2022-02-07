for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s = 0
    s += a
    if c>=b:
        s += b
        c -= b
        if c%3==0:
            s += c//3
    else:
        s += c
        b -= c
        if b%3==0:
            s += b//3
    print(s)
