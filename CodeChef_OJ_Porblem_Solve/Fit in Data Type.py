for _ in range(int(input())):
    n, x = map(int,input().split())
    if n>=x:
        print(x)
    else:
        while x>n:
            x = x-n-1
        print(x)
