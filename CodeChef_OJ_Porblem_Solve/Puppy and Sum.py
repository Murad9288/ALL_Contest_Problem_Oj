try:    
    for _ in range(int(input())):
        d, n = map(int,input().split())
        c = n
        for i in range(d):
            c = (n*(n+1)) // 2
            n = c
        print(c)
except:
    pass
    
    
    
