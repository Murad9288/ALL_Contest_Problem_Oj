try:
    for _ in range(int(input())):
        n,x = map(int,input().split())
        li = list(map(int,input().split()))[:n]
        arr = sorted(li)[::-1]
        b = False
        sum = 0
        c = 0
        for i in range(n):
            sum += arr[i]
            c += 1
            if sum >= x:
                b = True
                break
        if b:
            print(c)
        else:
            print(-1)
except:
    pass
