try:
    for _ in range(int(input())):
        a,b = map(int,input().split())
        a2,b2 = map(int,input().split())
        a3,b3 = map(int,input().split())
        res = [(a+b),(a2+b2),(a3+b3)]
        print(max(res))
except:
    pass
