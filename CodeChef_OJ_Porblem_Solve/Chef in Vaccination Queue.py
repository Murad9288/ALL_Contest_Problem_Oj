for _ in range(int(input())):
    n,p,x,y = map(int,input().split())
    arr = list(map(int,input().split()))
    s = 0
    for i in range(p):
        if arr[i] == 1:
            s += y
        else:
            s += x
    print(s)
