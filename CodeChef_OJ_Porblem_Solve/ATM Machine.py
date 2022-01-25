for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))[:n]
    for i in arr:
        if i<=k:
            print(1,end="")
            k -= i
        else:
            print(0,end="")
    print()
