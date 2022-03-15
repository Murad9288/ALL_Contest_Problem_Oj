for _ in range(int(input())):
    n,m = map(int,input().split())
    if n%2 == 0:
        a = n//2
        b = n//2
    else:
        a = n//2
        b = n//2+1
    if m%2 == 0:
        c = m//2
        d = m//2
    else:
        c = m//2
        d = m//2+1
    print(a*c+b*d)
