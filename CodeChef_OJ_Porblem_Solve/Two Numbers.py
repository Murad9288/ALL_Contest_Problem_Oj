try:
    for _ in range(int(input())):
        a,b,n=list(map(int,input().split()))
        if n%2==0:
            print(max(a,b)//min(a,b))
        else:
            print(max(2*a,b)//min(2*a,b))
except:
    pass
