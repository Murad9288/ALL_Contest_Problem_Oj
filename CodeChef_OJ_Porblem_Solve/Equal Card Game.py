try:
    for _ in range(int(input())):
        n = int(input())
        card = 52
        c = 0
        while card  != n:
            if card%n == 0:
                break

            c += 1
            card -= 1
        print(c)
except:
    pass
