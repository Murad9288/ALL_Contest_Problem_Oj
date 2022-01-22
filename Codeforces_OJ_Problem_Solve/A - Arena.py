for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = min(arr)
    c = 0
    for i in arr:
        if i>m:
            c += 1
    print(c)





