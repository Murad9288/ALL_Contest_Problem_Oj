try:
    for _ in range(int(input())):
        a, b, m = map(int, input().split())
        a, b = min(a, b), max(a, b)
        m = m*(m + 1) // 2
        if a > m:
            print(a + b - 2 * m)
        else:
            print(b - a)
except:
    pass
