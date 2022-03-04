for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    c = 0
    for i in a:
        if i>9 and i<61:
            c += 1
    print(c)
