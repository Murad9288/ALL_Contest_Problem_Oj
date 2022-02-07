for _ in range(int(input())):
    a,b,c,p,q,r = map(int,input().split())
    res = (p+q+r)//2
    if p+b+c > res or a+q+c > res or a+b+r > res:
        print("YES")
    else:
        print("NO")
