try:
    n = int(input())
    arr =list(map(int,input().split())) [:n]
    s,e = map(int,input().split())
    print(*arr[(s-1):e])

except:
    pass
