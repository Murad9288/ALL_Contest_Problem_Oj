for _ in range(int(input())):
    n,k = map(int,input().split())
    li = list(map(int,input().split()))
    s = sorted(li)
    c = s[::-1]
    sum = 0
    res = 0
    for i in c:
        sum += n-i
        if sum<n:
            res += 1
    print(res)
