try:
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        if a == b+c:
            print("YES")
        elif c == a+b:
            print("YES")
        elif b == a+c:
            print("YES")
        else:
            print("NO")
except:
    pass
