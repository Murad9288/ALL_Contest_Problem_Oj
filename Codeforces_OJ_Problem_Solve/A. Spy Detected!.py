for _ in range(int(input())):
    n = int(input())
    arr =list(map(int,input().split())) [:n]
    c = 0
    for i in arr:
        if arr.count(i) == 1:
            c = arr.index(i)
    print(c+1)
