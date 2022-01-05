for _ in range(int(input())):
    n = int(input())
    if n%2050 != 0:
        print(-1)
    else:
        res = n//2050
        c = 0
        for  i in str(res):
            c += int(i)
        print(c)
