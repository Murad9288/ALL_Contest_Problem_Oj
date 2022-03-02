for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    c = 0
    for i in arr:
        c |= i
    print(c)
