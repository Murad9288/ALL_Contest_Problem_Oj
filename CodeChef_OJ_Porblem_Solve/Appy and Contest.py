try:
    for _ in range(int(input())):
        n, a, b, k = list(map(int,input().split()))
        c = 0
        c2 = 0
        for i in range(1, n + 1):
            if i % a == 0 and i % b != 0:
                c += 1
            elif i % b == 0 and i % a != 0:
                c2 += 1
            if c + c2 >= k:
                res = "Win"
            else:
                res = "Lose"
        print(res)

except:
    pass
