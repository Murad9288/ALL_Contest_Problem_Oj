for _ in range(int(input())):
    a,b = map(int,input().split())
    res = a//(b**2)
    if res<=18:
        print(1)
    elif res<=24:
        print(2)
    elif res<=29:
        print(3)
    else:
        print(4)
