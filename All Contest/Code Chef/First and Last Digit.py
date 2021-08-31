try:
    for _ in range(int(input())):
        n = input()
        s = str(n)
        res = n[::-1]
        print((int(res)%10 + (int(n)%10)))
except:
    pass
