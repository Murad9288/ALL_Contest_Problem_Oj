try:
    for _ in range(int(input())):
        n = int(input())
        arr = []
        for _ in range(3):
            ar = list(map(int,input().split())) [:3]
            arr.append(ar)
        if arr[0][0] == n and arr[1][1] == n and arr[2][2] == n:
            print(0)
            continue
        a = arr[1][0]+arr[2][0]+arr[2][1]
        b = arr[0][1]+arr[0][2]+arr[1][2]
        if a>b:
            print(a)
        else:
            print(b)
except:
    pass
