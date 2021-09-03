try:
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        li = list(map(int,input().split()))
        if a+b+c >= sum(li) and c<=a:
            print("YES")
        else:
            print("NO")
except:
    pass
