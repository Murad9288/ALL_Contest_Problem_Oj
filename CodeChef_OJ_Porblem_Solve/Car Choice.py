for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    arr = [a,b,c,d]
    c = 0
    c2 = 0
    for i in range(len(arr)):
        c += arr[2]/arr[0]
        c2 += arr[3]/arr[1]
    if c == c2:
        print(0)
    elif c>c2:
        print(1)
    else:
        print(-1)
