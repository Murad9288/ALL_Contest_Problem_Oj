for _ in range(int(input())):
    x,a,b = map(int,input().split())
    print((a+(max(100,x)-min(100,x))*b)*10)
