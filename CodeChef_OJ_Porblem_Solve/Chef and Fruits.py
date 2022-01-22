try:
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        if abs(a-b) <= c:
            print("0")
        else:
            print(abs(a-b)-c)
except:
    pass
