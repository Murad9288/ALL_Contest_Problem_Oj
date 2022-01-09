try:
    for _ in range(int(input())):
        n = int(input())
        c = 0
        for i in range(11,-1,-1):
            while n>=2**i:
                n -= 2**i
                c += 1
        print(c)
        
except:
    pass
