for _ in range(int(input())):
    a,b,x = map(int,input().split())

    if a > b:
        a, b = b, a

    res = False
    while a:
        if x == a or x == b:
            res = True
            break
        if a < x < b and x % a == b % a:
            res = True
            break
        b = b % a
        a, b = b, a

    if res:
        print("YES")
    else:
        print("NO")
