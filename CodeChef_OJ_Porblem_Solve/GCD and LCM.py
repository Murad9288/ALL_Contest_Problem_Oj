try:
    import math
    for _ in range(int(input())):
        a,b = map(int,input().split())
        res = (a*b)//math.gcd(a,b)
        print(math.gcd(a,b),res)
except:
    pass
