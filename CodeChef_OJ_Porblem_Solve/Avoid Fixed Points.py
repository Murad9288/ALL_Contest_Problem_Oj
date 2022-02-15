for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    c = 0
    for i in range(len(arr)):
        if arr[i] == (i+c+1):
            c += 1
    print(c)
