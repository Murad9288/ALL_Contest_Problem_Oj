for _ in range(int(input())):
    li = list(map(int,input().split()))
    li.sort()
    res = li[-1] - li[0] - li[1]
    print(li[0],li[1],res)
