for _ in range(int(input())):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))[:a]
    c = 0
    for i in range(a-1,-1,-1):
        if arr[i]<b:
            print(i+1)
            c += 1
            break
    if c == 0:
        print(0)
