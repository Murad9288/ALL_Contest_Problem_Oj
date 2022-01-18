try:
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if a>1000:
            r = a-((a*10)/100)
            print("%.6f"%(r*b))
        else:
            print("%.6f"%(a*b))
except:
    pass
