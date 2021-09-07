try:
    for _ in range(int(input())):
        n,a,b = map(int,input().split())
        s = str(input())
        result = s.count("0")*a + s.count("1")*b
        print(result)
except:
    pass
