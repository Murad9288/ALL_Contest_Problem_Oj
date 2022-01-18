try:
    for _ in range(int(input())):
        n = int(input())
        if n >= 1500:
            h = 500
            d = 0.98 * n
        else:
            h = 0.10 * n
            d = 0.90 * n
        print(n+h+d)
except:
    pass
