for _ in range(int(input())):
    r,g,b = map(int,input().split())
    ad = (r + g + b) // 2
    print(min(ad , r + g , r + b , g + b))
