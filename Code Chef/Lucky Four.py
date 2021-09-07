try:
    for _ in range(int(input())):
        n = int(input())
        x = str(n)
        c = 0
        for i in x:
            if i == "4":
                c += 1
        print(c)
except:
    pass
