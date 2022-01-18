try:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split())) [:n]
        m = min(arr)
        arr.remove(m)
        m2 = min(arr)
        print(m+m2)
except:
    pass
