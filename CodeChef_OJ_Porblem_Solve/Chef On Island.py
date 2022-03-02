for _ in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    x = a/c
    y = b/d
    if min(x,y)>=e:
        print("YES")
    else:
        print("NO")
