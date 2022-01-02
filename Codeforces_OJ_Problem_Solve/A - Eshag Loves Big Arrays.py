for _ in range (int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = min(arr)
    c = arr.count(m)
    print(n-c)
