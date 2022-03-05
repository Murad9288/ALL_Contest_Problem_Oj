for _ in range(int(input())):
    x,a,b,c = map(int,input().split())
    if a<=b and a<=c:
        if b<=c:
            print((x-1)*a+b)
        else:
            print((x-1)*a+c)
    elif b<= a and b<=c:
        if a<=c:
            print((x-1)*b+a)
        else:
            print((x-1)*b+c)
    elif c<=a and c<=b:
        if b<=a:
            print((x-1)*c+b)
        else:
            print((x-1)*c+a)
