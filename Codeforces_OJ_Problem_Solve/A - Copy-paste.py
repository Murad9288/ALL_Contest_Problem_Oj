for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split()))[:n])
    a = arr[0]
    c = 0
    for i in arr[1:]:
        c += (k - i)//a
    print(c)
