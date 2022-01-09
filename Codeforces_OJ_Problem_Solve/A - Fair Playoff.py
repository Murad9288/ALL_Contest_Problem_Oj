for _ in range(int(input())):
    s1, s2, s3, s4 = list(map(int,input().split()))
    a = max(s1,s2)
    b = max(s3,s4)
    c = min(s1,s2)
    d = min(s3,s4)
    mn = min(a,b)
    mx = max(c,d)
    if mx > mn:
        print("NO")
    else:
        print("YES")
