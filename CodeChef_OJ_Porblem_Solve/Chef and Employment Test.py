for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = sorted(list(map(int,input().split()))[:n])
    print(arr[(n+k)//2])
