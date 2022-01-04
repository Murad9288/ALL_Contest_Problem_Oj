for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    res = li[0]
    for i in range(1,n):
        res &= li[i]
    print(res)
