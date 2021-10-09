for _ in range(int(input())):
    n = int(input())
    d = input()
    c = 0
    r = n-d.count("0")
    for i in range(n):
        c += int(d[i])
    c += r
    if int(d[-1]) != 0:
        c -= 1
    print(c)
