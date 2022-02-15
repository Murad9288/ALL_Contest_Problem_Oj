for _ in range(int(input())):
    x = int(input())
    s = str(input())
    c=d=n=0
    for i in range(len(s)):
        if s[i] == "C":
            c += 1
        elif s[i] == "N":
            n += 1
        else:
            d += 1
    c = 2*c+d
    n = 2*n+d
    if c>n:
        print(60*x)
    elif c<n:
        print(40*x)
    else:
        print(55*x)
