for _ in range(int(input())):
    H,x,y,C = map(int,input().split())
    res = x+(y//2)
    if C >= H*res:
        print("YES")
    else:
        print("NO")
