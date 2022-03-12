for _ in range(int(input())):
    n = int(input())
    s = str(input())
    mod = 998244353
    arr = [0]*n
    p = 1
    if s[0] == "1":
        arr[0] = 1
    x = arr[0]
    for i in range(1,n):
        if s[i] == "1":
            x += i+1
        arr[i] = x
        arr[i] = arr[i] % 2
    res = 0
    for i in range(n-1,-1,-1):
        if arr[i] == 1:
            res += p
            res %= mod
        p *= 2
    p %= mod

    print(res%mod)
