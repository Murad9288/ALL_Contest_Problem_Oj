for _ in range(int(input())):
    a,b = map(int,input().split())
    if a>b:
        print(a+b)
    elif a == b:
        print(a)
    else:
        c = b//a
        d = a*c
        res = (d+b)//2
        print(res)
