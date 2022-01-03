for _ in range(int(input())):
    n, m, k = map(int,input().split())
    if n == 1:
        if m == 0 and k >= 2:
            print("YES")
        else:
            print("NO")

    elif m < n - 1 or m > n * (n - 1) / 2:
        print("NO")
    elif m < n * (n - 1) / 2 and m >= n - 1:
        if k >= 4:
            print("YES")
        else:
            print("NO")
    else:
        if k >= 3:
            print("YES")
        else:
            print("NO")


