try:
    for _ in range(int(input())):
        n = int(input())
        c = 1
        while (c * (c + 1) // 2 <= n):
            c += 1
        print(c - 1)
except:
    pass
