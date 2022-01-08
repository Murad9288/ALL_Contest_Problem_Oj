for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a > b:
        a, b = b, a
    if (c + 1) * a >= b:
        print("YES")
    else:
        print("NO")
