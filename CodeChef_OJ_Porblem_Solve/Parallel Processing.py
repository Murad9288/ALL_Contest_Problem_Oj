for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    r = sum(a)
    c = 0
    res = r
    for i in range(n):
        c += a[i]
        res = min(max(c,r - c),res)
    print(res)
