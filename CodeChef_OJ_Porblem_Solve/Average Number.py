for _ in range(int(input())):
    n, k, v = map(int, input().split())
    arr = list(map(int, input().split()))
    r = v*(n + k)
    s = sum(arr)
    res = (r - s)//k
    if res > 0 and ((r - s) % k == 0):
        print(d)
    else:
        print("-1")
