for _ in range(int(input())):
    n,x = map(int,input().split())
    a = 0
    b = 0
    if x%3 == 0:
        a = x//3
    elif x%3 == 1:
        a += (x//3) + 1
        b += 2
    elif x%3 == 2:
        a += (x//3)+1
        b += 1
    if a+b <= n:
        print("YES")
        print(a,b,n-(a+b))
    else:
        print("NO")
