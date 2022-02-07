for _ in range(int(input())):
    x = int(input())
    y = 0
    c = 0
    while y<x:
        y += pow(2,c)
        c += 1
    c += 1
    y = x+(pow(2,c))
    print(x,0,y)
