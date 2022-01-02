try:
    x=0
    y=0
    m=0
    for _ in range(int(input())):
        (a,b)=map(int,input().split())
        x += a
        y += b
        if x>y and m<x-y:
            res = 1
            m = x-y
        if y>x and m<y-x:
            res = 2
            m = y-x
    print(res,end=" ")
    print(m)
except:
    pass
