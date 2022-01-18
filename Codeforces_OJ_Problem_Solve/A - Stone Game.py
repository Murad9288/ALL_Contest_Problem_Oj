for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    mi = arr.index(min(arr))
    ma = arr.index(max(arr))
    if ma<mi:
        ma,mi = mi,ma
    print(min((1+ma),(n-mi),(mi+1+n-ma)))
