try:
    for _ in range(int(input())):
        x,y = map(int,input().split())
        if x == y:
            print(2*x-1)
        else:
            print(x+y)
except:
    pass
