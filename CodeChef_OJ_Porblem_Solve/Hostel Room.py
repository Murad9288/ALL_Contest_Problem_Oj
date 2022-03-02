for _ in range(int(input())):
    n,x = map(int, input().split())
    li = list(map(int, input().split()))
    res = x
    mx = x
    for i in li:
        if (i<0):
            res -= abs(i)
        else:
            res += i
            if res > mx:
                mx = res
    print(mx)
