try:
    for _ in range(int(input())):
        s = str(input())
        res = s[::-1]
        if s == res:
            print("wins")
        else:
            print("loses")
except:
    pass
