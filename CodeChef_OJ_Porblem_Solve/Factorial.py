try:
    for _ in range(int(input())):
        n = int(input())
        c = 0
        num = 5

        while ((n // num) >= 1):
            k = n // num
            c = c + k
            num = num * 5
        print(c)
except:
    pass
