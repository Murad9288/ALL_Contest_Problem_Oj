for _ in range(int(input())):
    x, y, z = sorted(list(map(int,input().split())))
    if z == y:
        print("YES")
        print(y,x,x)
    else:
        print("NO")
