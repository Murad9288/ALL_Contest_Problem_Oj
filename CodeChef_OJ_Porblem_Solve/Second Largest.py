try:
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        li = [a,b,c]
        print(sorted(li)[1])
except:
    pass
