for _ in range(int(input())):
    x,y,n,r = map(int,input().split())
    if r//y >= n:
        print(0,n)
    elif r//x < n:
        print(-1)
    else:
        c = (r-(y*n))//(x-y)
        if ((r-(y*n))%(x-y)) != 0:
            c += 1
        print(c,n-c)
