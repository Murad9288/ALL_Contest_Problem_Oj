for _ in range(int(input())):
    s = str(input())
    z = 0
    o = 0
    for i in s:
        if i == "0":
            z += 1
        else:
            o += 1
    if z == o:
        print(z-1)
    else:
        print(min(z,o))
