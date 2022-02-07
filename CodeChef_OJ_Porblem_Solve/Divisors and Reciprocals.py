for _ in range(int(input())):
    x,a,b = map(int,input().split())
    if x%a == 0:
        p = x//a
        d = b*p
        s = 0
        for i in range(1,int(d**0.5)+1):
            if s>x:
                break
            elif d%i == 0:
                s += i
                if d//i != i:
                    s += d//i
        if s!=x:
            print(-1)
        else:
            print(d)
    else:
        print(-1)
