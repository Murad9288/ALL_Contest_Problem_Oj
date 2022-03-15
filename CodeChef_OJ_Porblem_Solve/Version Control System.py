for _ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    c = 0
    c2 = 0
    for i in range(1, n+1):
        if i in arr and i in arr2:
            c += 1
        if i not in arr and i not in arr2:
            c2 += 1
    print(c,c2)



